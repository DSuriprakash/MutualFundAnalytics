-- Total NAV Records
SELECT COUNT(*) FROM nav_history;

-- Top 5 NAV Values
SELECT *
FROM nav_history
ORDER BY nav DESC
LIMIT 5;

-- Average NAV per Fund
SELECT
    amfi_code,
    AVG(nav) AS avg_nav
FROM nav_history
GROUP BY amfi_code;

-- Top Performing Funds
SELECT
    scheme_name,
    return_3yr_pct
FROM scheme_performance
ORDER BY return_3yr_pct DESC
LIMIT 10;

-- Transaction Summary
SELECT
    transaction_type,
    COUNT(*) AS total_transactions,
    SUM(amount_inr) AS total_amount
FROM investor_transactions
GROUP BY transaction_type;