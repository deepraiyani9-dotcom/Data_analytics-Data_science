# Show rating, movie average, and difference from average

SELECT 
    user_id,
    movie_name,
    rating,
    AVG(rating) OVER(PARTITION BY movie_name) AS movie_average,
    rating - AVG(rating) OVER(PARTITION BY movie_name) AS difference
FROM MovieRatings;