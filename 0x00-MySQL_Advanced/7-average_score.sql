-- This script creates a procedure that computes and store the average score for a student.

DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
	DECLARE total_score FLOAT;
	DECLARE n_projects INT;

	SELECT SUM(score), COUNT(*) INTO total_score, n_projects FROM corrections c where c.user_id = user_id;
	SELECT n_projects AS 'Number of Projects';
	SELECT total_score AS 'TOTALE';
	if n_projects > 0 THEN
		UPDATE users SET average_score = total_score / n_projects WHERE id = user_id;
	end if;

END$$

DELIMITER ;
