import pandas as pd

# Load data
df = pd.read_csv("data/raw/09_portfolio_holdings.csv")

print("Original Shape:", df.shape)

# Remove duplicates
df = df.drop_duplicates()

# Convert date column
df["portfolio_date"] = pd.to_datetime(df["portfolio_date"])

# Remove rows with missing stock name
df = df.dropna(subset=["stock_name"])

print("Cleaned Shape:", df.shape)

# Save cleaned file
df.to_csv(
    "data/processed/clean_portfolio_holdings.csv",
    index=False
)

print("Saved successfully!")