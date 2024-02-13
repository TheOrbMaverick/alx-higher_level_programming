-- This script computes the score average of all records in the table second_table
-- The result column name is 'average'
-- The database name will be passed as an argument of the mysql command

-- You can run this script using the cat command with mysql like this:
-- cat compute_average.sql | mysql -hlocalhost -uroot -p hbtn_0c_0

-- Compute the score average
SELECT AVG(score) AS average
FROM hbtn_0c_0.second_table;
