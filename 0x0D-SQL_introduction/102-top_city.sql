-- Display the top 3 temperatures in July and August
USE hbtn_0c_0

SELECT city, AVG(value) as avg_temp
FROM temperatures WHERE month in (7, 8)
GROUP BY city ORDER BY avg_temp DESC
LIMIT 3;
