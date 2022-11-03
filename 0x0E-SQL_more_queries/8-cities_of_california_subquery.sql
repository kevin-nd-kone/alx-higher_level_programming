-- SELECT all cities of californie
SELECT * FROM cities,states 
         WHERE states.name = 'California' 
         AND states.id = cities.state_id
         ORDER BY cities.id ASC;