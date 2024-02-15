-- This script lists all Comedy shows from the hbtn_0d_tvshows database

-- List all Comedy shows
SELECT tv.title FROM tv_shows AS tv
INNER JOIN tv_show_genres AS comedy ON tv.id = comedy.show_id

INNER JOIN tv_genres AS genre ON genre.id = comedy.genre_id WHERE genre.name = "Comedy"
ORDER BY tv.title;