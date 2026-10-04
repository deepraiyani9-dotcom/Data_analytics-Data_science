-- Generate dates for the next 7 days

WITH RECURSIVE CalendarDays AS (
    SELECT CURDATE() AS day_date
    
    UNION ALL
    
    SELECT DATE_ADD(day_date, INTERVAL 1 DAY)
    FROM CalendarDays
    WHERE day_date < DATE_ADD(CURDATE(), INTERVAL 6 DAY)
)
SELECT day_date
FROM CalendarDays;