# Generate every possible user-offer combination

CREATE TABLE users (
    id INT PRIMARY KEY,
    user_name VARCHAR(50)
);

    CREATE TABLE offers (
        id INT PRIMARY KEY,
        offer_title VARCHAR(100)
    );

    SELECT 
        users.user_name,
        offers.offer_title
    FROM users
    CROSS JOIN offers;