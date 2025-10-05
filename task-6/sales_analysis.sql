USE online_sales_db;
SELECT * FROM online_sales LIMIT 10;
SELECT 
    EXTRACT(YEAR FROM date) AS year,
    EXTRACT(MONTH FROM date) AS month,
    COUNT(transaction_id) AS order_count,
    SUM(units_sold) AS total_units_sold,
    SUM(total_revenue) AS monthly_revenue
FROM online_sales
GROUP BY EXTRACT(YEAR FROM date), EXTRACT(MONTH FROM date)
ORDER BY year, month;
SELECT 
    EXTRACT(YEAR FROM date) AS year,
    EXTRACT(MONTH FROM date) AS month,
    COUNT(DISTINCT transaction_id) AS order_count,  -- Unique orders
    SUM(units_sold) AS total_units_sold,
    SUM(total_revenue) AS monthly_revenue
FROM online_sales
GROUP BY EXTRACT(YEAR FROM date), EXTRACT(MONTH FROM date)
ORDER BY year, month;
SELECT 
    EXTRACT(YEAR FROM date) AS year,
    EXTRACT(MONTH FROM date) AS month,
    COUNT(DISTINCT transaction_id) AS order_count,
    SUM(units_sold) AS total_units_sold,
    SUM(total_revenue) AS monthly_revenue
FROM online_sales
GROUP BY year, month
ORDER BY year ASC, month ASC;
SELECT 
    EXTRACT(YEAR FROM date) AS year,
    EXTRACT(MONTH FROM date) AS month,
    payment_method,
    COUNT(DISTINCT transaction_id) AS order_count,
    SUM(total_revenue) AS monthly_revenue
FROM online_sales
GROUP BY year, month, payment_method
ORDER BY year ASC, month ASC, monthly_revenue ASC;
SELECT 
    EXTRACT(YEAR FROM date) AS year,
    EXTRACT(MONTH FROM date) AS month,
    COUNT(DISTINCT transaction_id) AS order_count,
    SUM(units_sold) AS total_units_sold,
    SUM(total_revenue) AS monthly_revenue
FROM online_sales
WHERE EXTRACT(YEAR FROM date) = 2024
GROUP BY year, month
ORDER BY year ASC, month ASC;
SELECT 
    EXTRACT(YEAR FROM date) AS year,
    EXTRACT(MONTH FROM date) AS month,
    COUNT(DISTINCT transaction_id) AS order_count,
    SUM(units_sold) AS total_units_sold,
    SUM(total_revenue) AS monthly_revenue
FROM online_sales
WHERE EXTRACT(MONTH FROM date) IN (1,2,3,4,5,6) 
GROUP BY year, month
ORDER BY year ASC, month ASC;
