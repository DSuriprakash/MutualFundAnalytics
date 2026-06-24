import pandas as pd

df = pd.read_csv("data/raw/08_investor_transactions.csv")

print("Original Shape:", df.shape)

# Date conversion
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"],
    errors="coerce"
)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Amount validation
df = df[df["amount_inr"] > 0]

# Standardize transaction types
df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.title()
)

print("Cleaned Shape:", df.shape)

df.to_csv(
    "data/processed/clean_investor_transactions.csv",
    index=False
)

print("Saved successfully!")
