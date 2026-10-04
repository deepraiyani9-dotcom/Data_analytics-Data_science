-- Find cities with average rating above 4.0

WITH CityRatings AS (
    SELECT 
        city,
        AVG(rating) AS avg_rating
    FROM ZomatoRestaurants
    GROUP BY city
)
SELECT 
    r.name,
    r.city,
    r.rating
FROM ZomatoRestaurants r
JOIN CityRatings c
ON r.city = c.city
WHERE c.avg_rating > 4.0;