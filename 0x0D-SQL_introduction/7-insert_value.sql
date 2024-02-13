-- This script inserts a new row into the table first_table in the specified database
-- The database name will be passed as an argument of the mysql command

-- You can run this script using the cat command with mysql like this:
-- cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0

-- Inserting a new row into first_table
INSERT INTO hbtn_0c_0.first_table (id, name) VALUES (89, 'Best School');
