"""
ETL Pipeline for Sales Data Processing

This DAG processes sales data from CSV files and generates aggregated reports
by product category. The pipeline includes data validation, transformation,
and output verification steps.

Author: [Tu Nombre]
Created: September 2025
"""

from datetime import datetime
from airflow.decorators import dag, task
import pandas as pd
from pathlib import Path

# Configuration constants
DATA_DIR = Path("/opt/airflow/data")
INPUT_FILE = DATA_DIR / "sales.csv"
OUTPUT_FILE = DATA_DIR / "report_sales_by_category.csv"

@dag(
    dag_id="demo_csv_to_report",
    start_date=datetime(2025, 1, 1),
    schedule=None,          # ejecútalo manualmente
    catchup=False,
    tags=["demo", "pandas", "csv"],
)
def pipeline_csv_to_report():

    @task()
    def validate_input():
        if not INPUT_FILE.exists():
            raise FileNotFoundError(f"No existe {INPUT_FILE}")
        return INPUT_FILE.stat().st_size

    @task()
    def transform_to_report(_filesize):
        df = pd.read_csv(INPUT_FILE)
        df["revenue"] = df["unit_price"] * df["qty"]
        report = (
            df.groupby("category", as_index=False)
              .agg(
                  total_qty=("qty", "sum"),
                  total_revenue=("revenue", "sum"),
                  orders=("order_id", "count"),
              )
              .sort_values("total_revenue", ascending=False)
        )
        OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
        report.to_csv(OUTPUT_FILE, index=False)
        return str(OUTPUT_FILE)

    @task()
    def list_outputs(path):
        p = Path(path)
        if not p.exists():
            raise FileNotFoundError(f"No se generó el reporte en {p}")
        return [str(p), f"bytes={p.stat().st_size}"]

    size = validate_input()
    out = transform_to_report(size)
    list_outputs(out)

pipeline_csv_to_report()
