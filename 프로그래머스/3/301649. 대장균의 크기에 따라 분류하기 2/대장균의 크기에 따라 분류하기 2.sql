-- 코드를 작성해주세요
SELECT 
    ID,
    CASE
        WHEN rn <= total_cnt * 0.25 THEN 'CRITICAL'
        WHEN rn <= total_cnt * 0.50 THEN 'HIGH'
        WHEN rn <= total_cnt * 0.75 THEN 'MEDIUM'
        ELSE 'LOW'
    END AS COLONY_NAME
FROM (
    SELECT 
        ID,
        ROW_NUMBER() OVER (ORDER BY SIZE_OF_COLONY DESC, ID ASC) AS rn,
        COUNT(*) OVER () AS total_cnt
    FROM ECOLI_DATA
)t
ORDER BY ID