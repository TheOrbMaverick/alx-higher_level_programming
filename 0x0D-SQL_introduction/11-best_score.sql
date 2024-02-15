-- This script lists all records with a score >= 10 in the table second_table in the database hbtn_0c_0
-- Results display both the score and the name, ordered by score (top first)
-- The database name will be passed as an argument of the mysql command

-- You can run this script using the cat command with mysql like this:
-- cat list_records_above_10.sql | mysql -hlocalhost -uroot -p hbtn_0c_0

-- List all records with score >= 10, displaying score and name, ordered by score
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
