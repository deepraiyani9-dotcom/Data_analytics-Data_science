# Show all orders, including duplicates

SELECT order_id, customer_name, amount, order_date
FROM AppOrders

UNION ALL

SELECT order_id, customer_name, amount, order_date
FROM InStoreOrders;