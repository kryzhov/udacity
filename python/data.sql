SELECT id, occurred_at, total_amt_usd
FROM orders.csv
LIMIT 10;

'SELECT id, account_id, total_amt_usd
FROM orders
ORDER BY total_amt_usd
LIMIT 5;

SELECT id, account_id, total
FROM orders
ORDER BY total desc
LIMIT 5;
