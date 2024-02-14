-- This script lists all shows from the hbtn_0d_tvshows_rate database by their rating sum

-- List all shows and their rating sum
SELECT tv_shows.title, SUM(ratings.rating) AS rating_sum
FROM tv_shows
JOIN ratings ON tv_shows.id = ratings.show_id
GROUP BY tv_shows.id, tv_shows.title
ORDER BY rating_sum DESC;
