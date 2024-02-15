-- This script updates the score of Bob to 10 in the table second_table
-- The database name will be passed as an argument of the mysql command

-- You can run this script using the cat command with mysql like this:
-- cat update_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0

-- Update the score of Bob to 10
UPDATE second_table
SET score = 10
WHERE name = 'Bob';
