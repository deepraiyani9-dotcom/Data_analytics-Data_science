# 3. Rank movies by rating within each genre

SELECT 
    movie_id,
    genre,
    rating,
    DENSE_RANK() OVER (
        PARTITION BY genre
        ORDER BY rating DESC
    ) AS rating_rank
FROM Movies;