-- Create a new user with password and certain privilleges

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANTS ALL PRIVILEGES ON *.* 'user_0d_1'@'localhost' WITH GRANT OPTION;