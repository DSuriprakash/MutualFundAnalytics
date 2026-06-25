import pandas as pd

# Load data
df = pd.read_csv("data/raw/03_aum_by_fund_house.csv")

print("Original Shape:", df.shape)

# Remove duplicates
df = df.drop_duplicates()

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# Remove rows with missing fund house
df = df.dropna(subset=["fund_house"])

print("Cleaned Shape:", df.shape)

# Save cleaned file
df.to_csv(
    "data/processed/clean_aum_by_fund_house.csv",
    index=False
)

print("Saved successfully!")