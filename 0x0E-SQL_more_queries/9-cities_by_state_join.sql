-- select data from two TABLE
SELECT cities.id, cities.name, states.name
       FROM states, cities
       ORDER BY cities.id ASC;