SELECT title
FROM movies JOIN ratings on movies.id = ratings.movie_id
WHERE id IN
    (SELECT movie_id
    FROM stars
    WHERE person_id IN
        (SELECT id
        FROM people
        WHERE name ="Chadwick Boseman"))
ORDER BY rating DESC, title
LIMIT 5;