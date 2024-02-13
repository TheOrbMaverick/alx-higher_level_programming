-- This script creates the table second_table in the database hbtn_0c_0 and inserts multiple rows
-- The database name will be passed as an argument of the mysql command

-- You can run this script using the cat command with mysql like this:
-- cat create_and_insert.sql | mysql -hlocalhost -uroot -p hbtn_0c_0

-- Set the delimiter to $$ to allow for creating procedures
DELIMITER $$

-- Check if the table exists, if not, create it
CREATE PROCEDURE create_second_table()
BEGIN
    IF NOT EXISTS (
        SELECT NULL
        FROM information_schema.tables
        WHERE table_schema = 'hbtn_0c_0'
        AND table_name = 'second_table'
    ) THEN
        CREATE TABLE hbtn_0c_0.second_table (
            id INT,
            name VARCHAR(256),
            score INT
        );
    END IF;
END $$

-- Reset the delimiter
DELIMITER ;

-- Call the stored procedure to create the table if it doesn't exist
CALL create_second_table();

-- Insert multiple rows into second_table
INSERT INTO hbtn_0c_0.second_table (id, name, score)
VALUES 
    (1, 'John', 10),
    (2, 'Alex', 3),
    (3, 'Bob', 14),
    (4, 'George', 8);
