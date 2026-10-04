-- CTE calculates total runs for each team in 2023

WITH TeamRuns AS (
    SELECT 
        team,
        SUM(runs) AS total_runs
    FROM IPLMatches
    WHERE match_year = 2023
    GROUP BY team
)
SELECT team, total_runs
FROM TeamRuns
WHERE total_runs > 2000;