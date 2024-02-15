-- Change the default character set and collation for the 'hbtn_0c_0' database
-- This ensures that all new tables created in this database will use UTF-8 encoding

ALTER DATABASE CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;