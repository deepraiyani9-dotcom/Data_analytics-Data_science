# Show unique customer names from both tables

SELECT customer_name
FROM AppOrders

UNION

SELECT customer_name
FROM InStoreOrders;

**screenshot**

![alt text](image-1.png)