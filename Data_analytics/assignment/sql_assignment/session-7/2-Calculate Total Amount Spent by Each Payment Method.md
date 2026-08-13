# Task: Calculate Total Amount Spent by Each Payment Method

'''

SELECT payment_method, SUM(amount) AS total_amount_spent
FROM transactions
GROUP BY payment_method;

'''

**screenshot**

![alt text](image-1.png)
