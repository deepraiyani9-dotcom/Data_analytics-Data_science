# Create CustomerSegments table
CREATE TABLE CustomerSegments (
    segment_id INT PRIMARY KEY,
    segment_name VARCHAR(50)
);


ALTER TABLE Users
ADD segment_id INT,
ADD FOREIGN KEY (segment_id) REFERENCES CustomerSegments(segment_id);

SELECT 
    Users.username,
    CustomerSegments.segment_name,
    SUM(Orders.amount) AS total_order_amount
FROM Users
JOIN CustomerSegments
    ON Users.segment_id = CustomerSegments.segment_id
JOIN Orders
    ON Users.user_id = Orders.user_id
GROUP BY Users.username, CustomerSegments.segment_name;