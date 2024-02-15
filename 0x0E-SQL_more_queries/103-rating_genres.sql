-- This script lists all genres in the hbtn_0d_tvshows_rate database by their rating sum

-- List all genres and their rating sum
SELECT name, SUM(rate) AS rating FROM tv_genres AS gen
INNER JOIN tv_show_genres AS shw ON shw.genre_id = gen.id
INNER JOIN tv_show_ratings AS rtg ON rtg.show_id = shw.show_id
GROUP BY name
ORDER BY rating DESC;
