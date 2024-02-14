-- This script lists all genres not linked to the show Dexter from the hbtn_0d_tvshows database

-- Get the genre IDs linked to the show Dexter
SET @dexter_genre_ids := (SELECT GROUP_CONCAT(tv_show_genres.genre_id) FROM tv_show_genres JOIN tv_shows ON tv_shows.id = tv_show_genres.tv_show_id WHERE tv_shows.title = 'Dexter');

-- List all genres not linked to the show Dexter
SELECT tv_genres.name
FROM tv_genres
WHERE FIND_IN_SET(tv_genres.id, @dexter_genre_ids) = 0
ORDER BY tv_genres.name ASC;
