-- Create CTE TopArtists and select top 3 artists

WITH TopArtists AS (
    SELECT *
    FROM SpotifyArtists
    ORDER BY followers DESC
    LIMIT 3
)
SELECT *
FROM TopArtists;