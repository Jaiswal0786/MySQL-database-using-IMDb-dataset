CREATE PROCEDURE GetTitleStatsByYearAndType(
    IN p_title_type VARCHAR(50),
    IN p_year INTEGER
)
BEGIN
    SELECT T.start_year, G.genre, COUNT(DISTINCT T.title_id) AS Number_of_titles
    FROM Titles AS T
    JOIN Title_genres AS G ON T.title_id = G.title_id
    WHERE T.title_type = p_title_type
    AND T.start_year <= p_year
    GROUP BY T.start_year, G.genre
    ORDER BY T.start_year DESC, G.genre ASC;
END;

CREATE PROCEDURE Rating(
    IN p_rating FLOAT,
    IN p_id VARCHAR(50)
)
BEGIN
    UPDATE Title_ratings
    SET average_rating = (average_rating * num_votes + p_rating) / (num_votes + 1),
        num_votes = num_votes + 1
    WHERE title_id = p_id;
END;

