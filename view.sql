   
CREATE OR REPLACE VIEW order_summery AS
SELECT o.id AS ID, o.total_cost, o.created, p.first_name, p.last_name
FROM `Order` o
JOIN 
	Profile p ON o.profile_id = p.id
	
SELECT * FROM order_summery WHERE created > '2024-01-01';