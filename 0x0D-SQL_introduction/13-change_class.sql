-- This script removes all records with a score <= 5 in the table second_table
-- The database name will be passed as an argument of the mysql command

-- You can run this script using the cat command with mysql like this:
-- cat remove_records.sql | mysql -hlocalhost -uroot -p hbtn_0c_0

-- Remove all records with score <= 5
DELETE FROM second_table
WHERE score <= 5;
