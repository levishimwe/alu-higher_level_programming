-- List all genres not linked to the show Dexter
SELECT DISTINCT name
FROM tv_genres
WHERE name NOT IN
    (SELECT g.name
     FROM tv_genres g
     INNER JOIN tv_show_genres sg ON g.id = sg.genre_id
     INNER JOIN tv_shows s ON sg.show_id = s.id
     WHERE s.title = 'Dexter')
ORDER BY name ASC;
