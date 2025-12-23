from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]

from bootcamp_data.config import make_paths
from bootcamp_data.io import read_orders_csv, read_users_csv, write_parquet
from bootcamp_data.transforms import enforce_schema

# from src.bootcamp_data.config import make_paths
# from src.bootcamp_data.io import read_orders_csv, read_users_csv, write_parquet
# from src.bootcamp_data.transforms import enforce_schema

def main() -> None:
    p = make_paths(ROOT)
    orders:pd.DataFrame = enforce_schema(read_orders_csv(p.raw / "orders.csv"))
    users:pd.DataFrame = read_users_csv(p.raw / "users.csv")
    
    df_orders = orders.copy()

    print(df_orders)



    # out_orders = p.processed / "t-orders.parquet"
    # out_users = p.processed / "t-users.parquet"
    # write_parquet(orders, out_orders)
    # write_parquet(users, out_users)



if __name__ == "__main__":
    main()