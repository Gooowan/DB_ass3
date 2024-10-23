
CREATE FUNCTION GetPaidOrders(profileID INT)
RETURNS INT
DETERMINISTIC
BEGIN
    DECLARE paid_orders_count INT;

    SELECT COUNT(*)
    INTO paid_orders_count
    FROM `Order`
    WHERE profile_id = profileID AND paid = TRUE;

    RETURN paid_orders_count;
END;

SELECT GetPaidOrders(10557) AS paid_orders_count;