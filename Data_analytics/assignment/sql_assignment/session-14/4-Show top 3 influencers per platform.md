#  Show top 3 influencers per platform

SELECT 
    id,
    platform,
    followers,
    row_num
FROM (
    SELECT 
        id,
        platform,
        followers,
        ROW_NUMBER() OVER (
            PARTITION BY platform
            ORDER BY followers DESC
        ) AS row_num
    FROM Influencers
) AS RankedInfluencers
WHERE row_num <= 3;