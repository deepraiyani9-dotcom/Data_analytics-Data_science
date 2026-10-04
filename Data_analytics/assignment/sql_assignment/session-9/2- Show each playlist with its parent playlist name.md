# Show each playlist with its parent playlist name

SELECT 
    p.playlist_name AS playlist,
    parent.playlist_name AS parent_playlist
FROM playlists p
LEFT JOIN playlists parent
ON p.parent_playlist_id = parent.id;
