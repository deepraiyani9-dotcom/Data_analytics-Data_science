# Find restaurants with rating higher than average

SELECT name, rating
FROM Restaurants
WHERE rating > (
    SELECT AVG(rating)
    FROM Restaurants
);


**screenshot**
![alt text](image.png)