-- select element and group them by score VALUES
SELECT score,COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;