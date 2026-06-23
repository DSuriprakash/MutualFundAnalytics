import requests
import pandas as pd
import os

# Create folder if it doesn't exist
os.makedirs("data/raw", exist_ok=True)

# Mutual Fund Scheme Codes
funds = {
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for fund_name, scheme_code in funds.items():
    url = f"https://api.mfapi.in/mf/{scheme_code}"

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        if "data" in data:
            df = pd.DataFrame(data["data"])

            file_path = f"data/raw/{fund_name}.csv"
            df.to_csv(file_path, index=False)

            print(f"Saved: {file_path}")

        else:
            print(f"No data found for {fund_name}")

    except Exception as e:
        print(f"Error fetching {fund_name}: {e}")