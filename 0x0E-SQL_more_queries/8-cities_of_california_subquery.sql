-- This script lists all the cities of California from the database hbtn_0d_usa

-- Select the id of California from the states table
SET @california_id := (SELECT id FROM states WHERE name = 'California');

-- List all the cities of California
SELECT *
FROM cities
WHERE state_id = @california_id
ORDER BY cities.id ASC;
