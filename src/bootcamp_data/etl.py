from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class ETLConfig:
    root: Path
    raw_orders: Path
    raw_users: Path
    out_orders_clean: Path
    out_users: Path
    out_analytics: Path
    run_meta: Path
    
import pandas as pd
from bootcamp_data.io import read_orders_csv, read_users_csv

def load_inputs(cfg: ETLConfig) -> tuple[pd.DataFrame, pd.DataFrame]:
    orders = read_orders_csv(cfg.raw_orders)
    users = read_users_csv(cfg.raw_users)
    return orders, users


import pandas as pd

from bootcamp_data.quality import require_columns, assert_non_empty, assert_unique_key
from bootcamp_data.transforms import (
    enforce_schema,
    add_missing_flags,
    normalize_text,
    apply_mapping,
    parse_datetime,
    add_time_parts,
    winsorize,
    add_outlier_flag,
)
from bootcamp_data.joins import safe_left_join


def transform(orders_raw: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    # Fail-fast checks (before doing work)
    require_columns(
        orders_raw,
        ["order_id", "user_id", "amount", "quantity", "created_at", "status"],
    )
    require_columns(users, ["user_id", "country", "signup_date"])
    assert_non_empty(orders_raw, "orders_raw")
    assert_non_empty(users, "users")

    # The “one” side must be unique for a many→one join
    assert_unique_key(users, "user_id")

    status_map = {"paid": "paid", "refund": "refund", "refunded": "refund"}

    orders = (
        orders_raw.pipe(enforce_schema)
        .assign(
            status_clean=lambda d: apply_mapping(normalize_text(d["status"]), status_map)
        )
        .pipe(add_missing_flags, cols=["amount", "quantity"])
        .pipe(parse_datetime, col="created_at", utc=True)
        .pipe(add_time_parts, ts_col="created_at")
    )
    joined = safe_left_join(
        orders,
        users,
        on="user_id",
        validate="many_to_one",
        suffixes=("", "_user"),
    )

    # Left join should not change row count
    assert len(joined) == len(orders), "Row count changed (join explosion?)"

    # Outliers: keep raw `amount`, add winsorized + outlier flag for analysis
    joined = joined.assign(amount_winsor=winsorize(joined["amount"]))
    joined = add_outlier_flag(joined, "amount", k=1.5)

    return joined