-- SELECT all cities of californie
SELECT id, name 
         FROM cities
         WHERE state_id  IN ( SELECT id FROM states WHERE name = 'California')
         ORDER BY id ASC;