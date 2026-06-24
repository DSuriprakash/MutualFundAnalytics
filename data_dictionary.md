# Data Dictionary

## nav_history

| Column | Description |
|----------|-------------|
| amfi_code | Unique fund identifier |
| date | NAV date |
| nav | Net Asset Value |

## scheme_performance

| Column | Description |
|----------|-------------|
| amfi_code | Fund code |
| scheme_name | Fund name |
| return_1yr_pct | 1 year return |
| return_3yr_pct | 3 year return |
| return_5yr_pct | 5 year return |
| sharpe_ratio | Risk adjusted return |
| aum_crore | Assets under management |

## investor_transactions

| Column | Description |
|----------|-------------|
| investor_id | Investor ID |
| transaction_date | Transaction date |
| transaction_type | Purchase/Redemption/SIP |
| amount_inr | Transaction amount |
| state | Investor state |
| city | Investor city |