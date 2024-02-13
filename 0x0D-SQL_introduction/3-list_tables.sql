-- Script to list all tables of a specified database in MySQL server

-- Query to list tables
-- Retrieve table names from the information_schema.tables view
-- Filter by the specified database name
SELECT table_name FROM information_schema.tables WHERE table_schema = '$$DATABASE_NAME$$';
