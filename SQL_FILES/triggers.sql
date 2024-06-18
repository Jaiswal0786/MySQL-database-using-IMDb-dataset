DELIMITER //
CREATE TRIGGER update_show_rating_trigger AFTER INSERT ON Episode_belongs_to
FOR EACH ROW
BEGIN
    DECLARE total_ratings INTEGER;
    DECLARE new_average_rating FLOAT;

    -- Get the total number of votes and average rating for the parent show
    SELECT AVG(average_rating)
    INTO new_average_rating
    FROM Title_ratings
    WHERE title_id in (select e.episode_title_id from episode_belongs_to e where e.parent_tv_show_title_id=NEW.parent_tv_show_title_id);
    -- Update the Title_ratings table for the parent show with the new values
    UPDATE Title_ratings
    SET average_rating = new_average_rating
    WHERE title_id = NEW.parent_tv_show_title_id;
END;
//
DELIMITER ;