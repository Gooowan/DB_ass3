CREATE PROCEDURE GetUsersLiked(IN profileID INT)
BEGIN
    SELECT lp.profile_id, p.first_name, p.last_name, prod.name
    FROM `Liked_Products` lp
    JOIN Profile p ON lp.profile_id=p.id
    JOIN Product prod ON lp.product_id=prod.id
    
    WHERE lp.profile_id = profileID;
END;
CALL GetUsersLiked(67558);



CREATE PROCEDURE GetProductLikedByName(IN input_username VARCHAR(50))
BEGIN
	SELECT u.username, prof.first_name, prof.last_name, prod.name 
    FROM `User` u
	JOIN `Profile` prof ON u.profile_id = prof.id
	JOIN `Liked_Products` lp ON lp.profile_id = u.profile_id
	JOIN `Product` prod ON lp.product_id = prod.id
	WHERE u.username = input_username;
END;
CALL GetProductLikedByName('ejohnson');
