#    Find pairs of users living in the same city

SELECT 
    u1.name AS user1,
    u2.name AS user2,
    u1.city
FROM users u1
JOIN users u2
ON u1.city = u2.city
AND u1.id < u2.id;
