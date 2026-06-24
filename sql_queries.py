import sqlite3
import pandas as pd

conn = sqlite3.connect("mutualfund.db")

# 1. Count records
query1 = "SELECT COUNT(*) FROM nav_history"
print("Total Rows:", pd.read_sql(query1, conn))

# 2. Top NAV values
query2 = """
SELECT * FROM nav_history
ORDER BY nav DESC
LIMIT 5
"""
print("\nTop NAV Values:")
print(pd.read_sql(query2, conn))

# 3. Sample per fund
query3 = """
SELECT amfi_code, AVG(nav) as avg_nav
FROM nav_history
GROUP BY amfi_code
LIMIT 5
"""
print("\nAverage NAV per fund:")
print(pd.read_sql(query3, conn))

conn.close()