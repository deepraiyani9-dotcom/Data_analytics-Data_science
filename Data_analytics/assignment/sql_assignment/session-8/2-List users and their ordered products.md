# List users and their ordered products

SELECT Users.username, Orders.product
FROM Users
INNER JOIN Orders
ON Users.user_id = Orders.user_id;

**screenshot**

c:\Users\DELL\OneDrive\Pictures\Screenshots\Screenshot 2026-10-04 085024.png
