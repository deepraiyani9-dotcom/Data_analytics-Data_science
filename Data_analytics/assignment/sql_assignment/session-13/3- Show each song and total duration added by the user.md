# Show each song and total duration added by the user

SELECT 
    song_id,
    user_id,
    duration_sec,
    SUM(duration_sec) OVER(PARTITION BY user_id) AS total_duration
FROM Playlist;

