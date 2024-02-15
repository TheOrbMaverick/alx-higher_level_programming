-- This script lists all shows without the genre Comedy from the hbtn_0d_tvshows database

-- Get the show IDs linked to the genre Comedy
SET @comedy_show_ids := (SELECT GROUP_CONCAT(tv_shows.id) FROM tv_shows JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id WHERE tv_genres.name = 'Comedy');

-- List all shows without the genre Comedy
SELECT tv_shows.title
FROM tv_shows
WHERE tv_shows.id NOT IN (SELECT show_id FROM tv_show_genres WHERE show_id IN (SELECT * FROM FIND_IN_SET(show_id, @comedy_show_ids)))
ORDER BY tv_shows.title ASC;
