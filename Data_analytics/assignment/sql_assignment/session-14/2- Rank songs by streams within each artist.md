# 2. Rank songs by streams within each artist

SELECT 
    song_id,
    artist,
    streams,
    RANK() OVER (
        PARTITION BY artist
        ORDER BY streams DESC
    ) AS song_rank
FROM Songs;