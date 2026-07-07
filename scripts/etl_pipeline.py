"""
ETL Pipeline for Mutual Fund Analytics
Author: D Suri Prakash
"""

import subprocess
import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent

scripts = [
    "data_ingestion.py",
    "clean_fund_master.py",
    "clean_scheme_performance.py",
    "clean_portfolio_holdings.py",
    "clean_monthly_sip_inflows.py",
    "clean_category_inflows.py",
    "clean_aum_by_fund_house.py",
    "clean_benchmark_indices.py",
    "clean_industry_folio_count.py",
    "clean_investor_transactions.py",
    "database.py"
]

for script in scripts:
    print(f"Running {script}...")
    subprocess.run([sys.executable, str(project_root / script)], check=True)

print("\nETL Pipeline Completed Successfully!")