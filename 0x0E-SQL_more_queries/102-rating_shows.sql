-- This script lists all shows from the hbtn_0d_tvshows_rate database by their rating sum

-- List all shows and their rating sum

SELECT title, SUM(rate) AS rating
  FROM tv_shows AS tite
       INNER JOIN tv_show_ratings AS rates
       ON tite.id = rates.show_id
 GROUP BY title
 ORDER BY rating DESC;