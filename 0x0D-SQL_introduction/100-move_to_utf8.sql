-- Switch to the 'hbtn_0c_0' database
-- This sets the default database context for subsequent SQL statements
USE hbtn_0c_0;

-- Change the default character set and collation for the 'hbtn_0c_0' database
-- This ensures that all new tables created in this database will use UTF-8 encoding
ALTER DATABASE CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Change the character set and collation for the 'first_table' table
-- This ensures that all existing data in this table is converted to UTF-8 encoding
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;