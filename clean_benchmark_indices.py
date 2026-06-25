import pandas as pd

# Load data
df = pd.read_csv("data/raw/10_benchmark_indices.csv")

print("Original Shape:", df.shape)

# Remove duplicates
df = df.drop_duplicates()

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# Remove rows with missing index name
df = df.dropna(subset=["index_name"])

print("Cleaned Shape:", df.shape)

# Save cleaned file
df.to_csv(
    "data/processed/clean_benchmark_indices.csv",
    index=False
)

print("Saved successfully!")