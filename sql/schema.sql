CREATE TABLE nav_history (
    amfi_code INTEGER,
    date DATE,
    nav REAL
);

CREATE TABLE scheme_performance (
    amfi_code INTEGER,
    scheme_name TEXT,
    fund_house TEXT,
    category TEXT,
    return_1yr_pct REAL,
    return_3yr_pct REAL,
    return_5yr_pct REAL,
    sharpe_ratio REAL,
    aum_crore REAL
);

CREATE TABLE investor_transactions (
    investor_id INTEGER,
    transaction_date DATE,
    amfi_code INTEGER,
    transaction_type TEXT,
    amount_inr REAL,
    state TEXT,
    city TEXT
);