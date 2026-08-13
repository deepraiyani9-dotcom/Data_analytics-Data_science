# Task: Find Genres with Box Office Collection Above 10 Crore

'''

SELECT genre, SUM(box_office_collection) AS total_box_office_collection
FROM movies
GROUP BY genre
HAVING SUM(box_office_collection) > 10;

'''

**screenshot**

![alt text](image-2.png)