import pandas as pd

# Load data
df = pd.read_csv("data/raw/05_category_inflows.csv")

print("Original Shape:", df.shape)

# Remove duplicates
df = df.drop_duplicates()

# Convert month column
df["month"] = pd.to_datetime(df["month"])

# Remove rows with missing category
df = df.dropna(subset=["category"])

print("Cleaned Shape:", df.shape)

# Save cleaned file
df.to_csv(
    "data/processed/clean_category_inflows.csv",
    index=False
)

print("Saved successfully!")