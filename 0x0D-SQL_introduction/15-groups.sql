-- This script lists the number of records with the same score in the table second_table
-- The result displays the score and the number of records for this score with the label 'number'
-- The list is sorted by the number of records (descending)
-- The database name will be passed as an argument of the mysql command

-- You can run this script using the cat command with mysql like this:
-- cat list_score_count.sql | mysql -hlocalhost -uroot -p hbtn_0c_0

-- List the number of records with the same score
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
