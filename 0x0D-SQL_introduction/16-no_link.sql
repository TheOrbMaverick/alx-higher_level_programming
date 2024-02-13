-- This script lists all records of the table second_table excluding rows without a name value
-- Results display the score and the name, in descending order of score
-- The database name will be passed as an argument of the mysql command

-- You can run this script using the cat command with mysql like this:
-- cat list_records_with_name.sql | mysql -hlocalhost -uroot -p hbtn_0c_0

-- List all records with name value, displaying score and name, ordered by score (descending)
SELECT score, name
FROM hbtn_0c_0.second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
