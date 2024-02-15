-- This script lists all Comedy shows from the hbtn_0d_tvshows database

-- List all Comedy shows
SELECT shows.title FROM tv_shows AS shows
INNER JOIN tv_show_genres ON shows.id = tv_show_genres.show_id

INNER JOIN tv_genres ON tv_show_genres.id = tv_show_genres.id
WHERE tv_genres.name = 'Comedy'
ORDER BY shows.title ASC;
