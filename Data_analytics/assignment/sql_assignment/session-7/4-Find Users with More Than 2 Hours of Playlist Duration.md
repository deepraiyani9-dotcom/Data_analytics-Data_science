# Task: Find Users with More Than 2 Hours of Playlist Duration

'''

SELECT user_id, SUM(duration) AS total_duration
FROM playlist
GROUP BY user_id
HAVING SUM(duration) > 7200;

'''

**screenshot**

![alt text](image-3.png)