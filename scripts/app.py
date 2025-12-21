from src.bootcamp_data.io import read_orders_csv
from src.bootcamp_data.io import write_parquet
from pathlib import Path

import pandas as pd
ROOT = Path(__file__).resolve().parents[1]

path = Path("data//raw/orders.csv")
df = read_orders_csv(path)
print(df)
print(ROOT)
# print(Path.chmod())
