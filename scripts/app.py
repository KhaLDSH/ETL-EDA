from src.bootcamp_data.config import make_paths
# from bootcamp_data.io import write_parquet
from pathlib import Path
import sys

import pandas as pd
ROOT = Path(__file__).resolve().parents[1]

# path = Path("data//raw/orders.csv")
# df = read_orders_csv(path)
# print(df)
print("\n",ROOT, "")
print(sys.executable)
# print("\n\n",make_paths(ROOT), "\n\n")
