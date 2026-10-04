-- Calculate monthly sales and find the highest month

WITH MonthlyTotals AS (
    SELECT 
        MONTH(order_date) AS month,
        SUM(total_amount) AS total_sales
    FROM FlipkartOrders
    WHERE YEAR(order_date) = 2023
    GROUP BY MONTH(order_date)
)
SELECT *
FROM MonthlyTotals
ORDER BY total_sales DESC
LIMIT 1;