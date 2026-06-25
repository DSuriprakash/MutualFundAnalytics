import pandas as pd

# Load data
df = pd.read_csv("data/raw/04_monthly_sip_inflows.csv")

print("Original Shape:", df.shape)

# Remove duplicates
df = df.drop_duplicates()

# Convert month column
df["month"] = pd.to_datetime(df["month"])

print("Cleaned Shape:", df.shape)

# Save cleaned file
df.to_csv(
    "data/processed/clean_monthly_sip_inflows.csv",
    index=False
)

print("Saved successfully!")