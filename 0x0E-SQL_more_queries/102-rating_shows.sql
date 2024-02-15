-- This script lists all shows from the hbtn_0d_tvshows_rate database by their rating sum

-- List all shows and their rating sum
SELECT title, SUM(rate) AS rating_sum
FROM tv_shows
INNER JOIN tv_show_ratings ON title.id = tv_show_ratings.show_id
GROUP BY title
ORDER BY rating_sum DESC;
