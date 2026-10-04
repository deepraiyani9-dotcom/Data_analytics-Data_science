# Show all orders with username using RIGHT JOIN

SELECT Orders.order_id, Users.username
FROM Users
RIGHT JOIN Orders
ON Users.user_id = Orders.user_id;

**screenshot**

![alt text](image-1.png)