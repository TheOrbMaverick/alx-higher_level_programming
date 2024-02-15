-- This script lists all Comedy shows from the hbtn_0d_tvshows database

-- List all Comedy shows
SELECT tv.title 
    FROM tv_shows AS tv
        INNER JOIN tv_show_genres AS shows 
        ON tv.id = shows.show_id

    INNER JOIN tv_genres as gen
    ON gen.id = shows.genre_id
    WHERE gen.name = 'Comedy'
    ORDER BY tv.title;
