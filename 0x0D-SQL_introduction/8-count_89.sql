-- This script displays the number of records with id = 89 in the table first_table
-- The database name will be passed as an argument of the mysql command

-- You can run this script using the cat command with mysql like this:
-- cat count_records.sql | mysql -hlocalhost -uroot -p hbtn_0c_0

-- Counting the number of records with id = 89 in first_table
SELECT COUNT(*) AS record_count
FROM hbtn_0c_0.first_table
WHERE id = 89;
