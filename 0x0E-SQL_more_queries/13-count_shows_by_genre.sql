-- This script lists all genres from the hbtn_0d_tvshows database and displays the number of shows linked to each

-- List all genres and the number of shows linked to each
SELECT genres.genre AS genre,
       COUNT(tv_show_genres.show_id) AS number_of_shows
FROM genres
JOIN tv_show_genres ON genres.id = tv_show_genres.genre_id
GROUP BY genres.id, genres.genre
ORDER BY number_of_shows DESC;
