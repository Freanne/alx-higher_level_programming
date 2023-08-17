-- 5-unique_id.sql

USE hbtn_0d_2;  -- Use the specified database

-- Create the table 'unique_id' if it doesn't exist
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256),
    PRIMARY KEY (id)
);
