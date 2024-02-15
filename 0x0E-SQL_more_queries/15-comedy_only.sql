-- This script lists all Comedy shows from the hbtn_0d_tvshows database

-- List all Comedy shows
SELECT tv.title
  FROM tv_shows AS tv
       INNER JOIN tv_show_genres AS s
       ON tv.id = s.show_id

       INNER JOIN tv_genres AS genre
       ON genre.id = s.genre_id
       WHERE genre.name = "Comedy"
 ORDER BY tv.title;