import pandas as pd

def enforce_schema(df: pd.DataFrame) -> pd.DataFrame:
    return df.assign(
        order_id= df["oreder_id"].astype("string"),
        user_id= df["user_id"].astype("string"),
        amount= pd.to_numeric(df["amount"], errors="coerce").astype("Float64"),
        quantity= pd.to_numeric(df["quantity"], errors="coerce").astype("Float64")
    )