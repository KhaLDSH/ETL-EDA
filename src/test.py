import bootcamp_data.yes as yes
yes

import pandas as pd


df = pd.read_parquet("data/processed/analytics_table.parquet")

print("rows:", len(df))
print("cols:", len(df.columns), "\n-------------")
print(df.dtypes)


# def describe_numeric(df: pd.DataFrame, col: str) -> pd.Series:
#     s = pd.to_numeric(df[col], errors="coerce")
#     return pd.Series({
#         "n": s.notna().sum(),
#         "mean": s.mean(),
#         "median": s.median(),
#         "p25": s.quantile(0.25),
#         "p75": s.quantile(0.75),
#         "p90": s.quantile(0.90),
#         "min": s.min(),
#         "max": s.max(),
#     })

# print(describe_numeric(df, "amount"))

# from __future__ import annotations

import numpy as np
import pandas as pd

def bootstrap_diff_means(
    a: pd.Series,
    b: pd.Series,
    *,
    n_boot: int = 2000,
    seed: int = 0,
) -> dict[str, float]:
    """Bootstrap CI for the difference in means (A - B).

    For rates, pass a 0/1 Series (e.g., `is_refund.astype(int)`).
    """
    rng = np.random.default_rng(seed) #Random number generator
    a = pd.to_numeric(a, errors="coerce").dropna().to_numpy()
    b = pd.to_numeric(b, errors="coerce").dropna().to_numpy()
    assert len(a) > 0 and len(b) > 0, "Empty group after cleaning"

    diffs = []
    for _ in range(n_boot):
        # Pick a random sample from the array `a` with replacement 
        # The sample size is the full list
        sa = rng.choice(a, size=len(a), replace=True) 
        sb = rng.choice(b, size=len(b), replace=True)
        diffs.append(sa.mean() - sb.mean())
    diffs = np.array(diffs)

    return {
        "diff_mean": float(a.mean() - b.mean()),
        "ci_low": float(np.quantile(diffs, 0.025)),
        "ci_high": float(np.quantile(diffs, 0.975)),
    }

d = df.assign(is_refund=df["status_clean"].eq("refund"))

a = d.loc[d["country"].eq("SA"), "is_refund"].astype(int)
b = d.loc[d["country"].eq("AE"), "is_refund"].astype(int)

print("n_SA:", len(a), "n_AE:", len(b))

res = bootstrap_diff_means(a, b, n_boot=2000, seed=0)
print(res)