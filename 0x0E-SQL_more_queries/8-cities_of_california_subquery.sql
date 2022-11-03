-- SELECT all cities of californie
SELECT cities.id, cities.state_id, cities.name 
         FROM cities,states 
         WHERE states.name = 'California' 
         AND states.id = cities.state_id
         ORDER BY cities.id ASC;