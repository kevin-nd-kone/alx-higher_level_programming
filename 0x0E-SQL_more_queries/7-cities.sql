-- Create database and TABLE
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE Table IF NOT EXISTS cites(id INT PRIMARY KEY AUTO_INCREMENT NOT NULL UNIQUE,
                                state_id int NOT NULL FOREIGN KEY REFERENCES states ON id,
                                name VARCHAR(256) NOT NULL);