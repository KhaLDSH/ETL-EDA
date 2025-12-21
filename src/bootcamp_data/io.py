import pandas as pd
from pathlib import Path

NA = ["", "NA", "N/A", "null", "None", "not-a-number"]
def read_orders_csv(path) -> pd.DataFrame:
    return pd.read_csv(
        path,
        dtype={"order_id":"string", "user_id":"string"},
        na_values=NA,
        keep_default_na=True
    )

def read_users_csv(path) -> pd.DataFrame:
    ...
    
def write_parquet(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(path, index=False)
    
def read_parquet(path) -> pd.DataFrame:
    ...


