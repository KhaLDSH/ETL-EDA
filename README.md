week2-AiPro
# ETL & EDA Pipeline 🧩📈

A structured project demonstrating **ETL (Extract, Transform, Load)** and **Exploratory Data Analysis (EDA)** workflows using Python.  
The repository focuses on clean data ingestion, transformation, validation, and exploratory analysis to prepare datasets for downstream analytics or machine learning tasks.

---

### 1. Prerequisites
Make sure you have the following installed:

- Python 3.10+
- [uv](https://github.com/astral-sh/uv) (recommended for dependency management)
- Git

---

### 2. Setup

**Clone** the repository and **navigate** to the project root:

```bash
git clone https://github.com/KhaLDSH/ETL-EDA.git
cd ETL-EDA
```

Install dependencies and set up the local environment:
```bash
uv sync
```


## Run ETL
```bash
uv run python scripts/run_etl.py
```

## Outputs
- data/processed/orders_clean.parquet
- data/processed/users.parquet
- data/processed/analytics_table.parquet
- data/processed/_run_meta.json
- reports/figures/*.png

## EDA
```bash
uv run jupyter notebook .\notebooks\eda.ipynb
```

***OR***
Open notebooks/eda.ipynb and run all cells.