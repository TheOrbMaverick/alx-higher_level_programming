-- This script prints the full description of the table first_table from the database hbtn_0c_0
-- The database name will be passed as an argument of the mysql command

-- You can run this script using the cat command with mysql like this:
-- cat 5-full_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0

-- First, we define a variable to hold the database name
SET @db_name := 'hbtn_0c_0';

-- Then we execute a query to retrieve the full table description
SELECT CONCAT('Table: first_table', '\n', 'Create Table: ', Create_Table)
FROM information_schema.tables
WHERE table_schema = @db_name
AND table_name = 'first_table';
