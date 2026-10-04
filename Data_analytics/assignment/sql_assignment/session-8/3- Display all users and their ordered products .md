# Display all users and their ordered products

SELECT Users.username, Orders.product
FROM Users
LEFT JOIN Orders
ON Users.user_id = Orders.user_id;

**screenshot**
![alt text](image.png)