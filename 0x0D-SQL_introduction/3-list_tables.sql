-- Script to list all tables of a specified database in MySQL server

-- Check if the correct database name is provided
-- Note: This script does not handle command-line arguments directly; the database name must be passed when executing the script using a shell command

-- Define the database name using a variable
SET @database_name = 'mysql';

-- Query to list tables
-- Retrieve table names from the information_schema.tables view
-- Filter by the specified database name
SELECT table_name FROM information_schema.tables WHERE table_schema = @database_name;
