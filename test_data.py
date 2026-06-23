import pandas as pd

df = pd.read_csv("data/raw/SBI_Bluechip.csv")

print(df.head())
print("\nShape:", df.shape)
print("\nColumns:", df.columns.tolist())