-- Script to list all tables of a specified database in MySQL server

-- Check if the correct number of arguments is provided
-- Usage: mysql -u <username> -p <password> -h <hostname> <database_name> < 3-list_tables.sql
SET @db_name = '$$mysql$$';

-- Query to list tables
-- Retrieve table names from the information_schema.tables view
-- Filter by the specified database name
SELECT table_name FROM information_schema.tables WHERE table_schema = @db_name;
