-- This script lists all genres from the hbtn_0d_tvshows database and displays the number of shows linked to each

-- List all genres and the number of shows linked to each
SELECT gen.genre AS genre,
       COUNT(*) AS number_of_shows
FROM tv_genres AS gen
INNER JOIN tv_show_genres AS geny ON gen.id = geny.genre_id
GROUP BY gen.genre
ORDER BY number_of_shows DESC;
