-- Script to create a table called first_table in the current database in MySQL server

-- Check if the table first_table does not exist
-- If the table exists, the script will not fail
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
