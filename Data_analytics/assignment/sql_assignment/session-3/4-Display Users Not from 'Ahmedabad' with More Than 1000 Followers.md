# Task: Display Users Not from 'Ahmedabad' with More Than 1000 Followers

```sql
SELECT *
FROM users
WHERE NOT city = 'Ahmedabad'
AND followers > 1000;
```

