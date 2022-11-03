-- Import data from sql file
--  < https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql
SET autocommit=0 ; source https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql ; COMMIT ;
SELECT state,MAX(value) as max_temp FROM temperatures GROUP BY city ORDER BY state ASC;