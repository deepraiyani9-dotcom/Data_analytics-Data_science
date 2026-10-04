# Add duplicate customer name in both tables

INSERT INTO AppOrders VALUES
(4, 'Neha', 300, '2026-10-04');

INSERT INTO InStoreOrders VALUES
(104, 'Neha', 300, '2026-10-04');

SELECT customer_name
FROM AppOrders
UNION
SELECT customer_name
FROM InStoreOrders;

SELECT customer_name
FROM AppOrders
UNION ALL
SELECT customer_name
FROM InStoreOrders;
