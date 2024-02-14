-- This script lists all genres in the hbtn_0d_tvshows_rate database by their rating sum

-- List all genres and their rating sum
SELECT tv_genres.name, SUM(ratings.rating) AS rating_sum
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_show_genres.tv_show_id = tv_shows.id
JOIN ratings ON tv_shows.id = ratings.show_id
GROUP BY tv_genres.id, tv_genres.name
ORDER BY rating_sum DESC;
