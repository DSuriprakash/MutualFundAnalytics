import pandas as pd

# Load data
df = pd.read_csv("data/raw/01_fund_master.csv")

print("Original Shape:", df.shape)

# Remove duplicates
df = df.drop_duplicates()

# Remove rows with missing AMFI code
df = df.dropna(subset=["amfi_code"])

print("Cleaned Shape:", df.shape)

# Save cleaned file
df.to_csv(
    "data/processed/clean_fund_master.csv",
    index=False
)

print("Saved successfully!")