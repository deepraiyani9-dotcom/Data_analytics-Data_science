# Show users who created more playlists than average

SELECT 
    u.username,
    p.playlist_count
FROM Users u
JOIN (
    SELECT user_id, COUNT(*) AS playlist_count
    FROM Playlists
    GROUP BY user_id
) p ON u.user_id = p.user_id
WHERE p.playlist_count > (
    SELECT AVG(playlist_count)
    FROM (
        SELECT user_id, COUNT(*) AS playlist_count
        FROM Playlists
        GROUP BY user_id
    ) x
);