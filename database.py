import sqlite3
import pandas as pd

# Load cleaned data
df = pd.read_csv("data/processed/clean_nav_history.csv")

# Create SQLite database
conn = sqlite3.connect("mutualfund.db")

# Save to SQL table
df.to_sql("nav_history", conn, if_exists="replace", index=False)

print("Data loaded into SQLite database successfully!")

# Verify
result = pd.read_sql("SELECT * FROM nav_history LIMIT 5", conn)
print(result)

conn.close()