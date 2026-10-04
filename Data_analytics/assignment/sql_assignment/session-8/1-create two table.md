CREATE TABLE Users (
    user_id INT PRIMARY KEY,
    username VARCHAR(100),
    city VARCHAR(100)
);

CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    user_id INT,
    product VARCHAR(100),
    amount DECIMAL(10,2),
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

INSERT INTO Users (user_id, username, city) VALUES
(1, 'Rahul', 'Ahmedabad'),
(2, 'Priya', 'Rajkot'),
(3, 'Amit', 'Surat');

INSERT INTO Orders (order_id, user_id, product, amount) VALUES
(101, 1, 'Laptop', 50000),
(102, 1, 'Mouse', 1000),
(103, 2, 'Keyboard', 2000),
(104, 2, 'Headphones', 3000),
(105, 2, 'Mobile', 25000);