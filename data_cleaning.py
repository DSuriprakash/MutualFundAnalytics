import pandas as pd

# Load data
df = pd.read_csv("data/raw/02_nav_history.csv")

print("Original Shape:", df.shape)

# 1. Convert date to datetime
df['date'] = pd.to_datetime(df['date'])

# 2. Remove duplicates
df = df.drop_duplicates()

# 3. Sort by amfi_code + date
df = df.sort_values(by=['amfi_code', 'date'])

# 4. Remove invalid NAV values
df = df[df['nav'] > 0]

# 5. Reset index
df = df.reset_index(drop=True)

print("\nCleaned Shape:", df.shape)

print("\nData Check:")
print(df.head())

# 6. Save cleaned file
df.to_csv("data/processed/clean_nav_history.csv", index=False)

print("\nSaved: data/processed/clean_nav_history.csv")