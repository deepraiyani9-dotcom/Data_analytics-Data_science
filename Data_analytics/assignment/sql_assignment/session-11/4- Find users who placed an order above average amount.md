# Find users who placed an order above average amount

SELECT DISTINCT user_id
FROM Orders
WHERE total_amount > (
    SELECT AVG(total_amount)
    FROM Orders
);

**screenshot**
![alt text](image-2.png)