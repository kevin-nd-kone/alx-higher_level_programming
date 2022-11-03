-- SELECT all cities of californie
SELECT id, state_id, name 
         FROM cities
         WHERE cities.state_id  IN ( SELECT id FROM states WHERE name = 'California')
         ORDER BY cities.id ASC;