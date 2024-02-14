-- This script lists all the cities of California from the hbtn_0d_usa database without using the JOIN keyword

-- Select the state ID for California
SET @california_id := (SELECT id FROM states WHERE name = 'California');

-- List all cities of California
SELECT *
FROM cities
WHERE state_id = @california_id
ORDER BY id ASC;
