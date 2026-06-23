import pandas as pd
import os

DATA_FOLDER = "data/raw"

print("=" * 50)
print("DATA INGESTION REPORT")
print("=" * 50)

for file in os.listdir(DATA_FOLDER):
    if file.endswith(".csv"):
        file_path = os.path.join(DATA_FOLDER, file)

        print(f"\nProcessing: {file}")

        df = pd.read_csv(file_path)

        print("Shape:", df.shape)
        print("Columns:", list(df.columns))

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("-" * 50)

print("\nData ingestion completed successfully!")