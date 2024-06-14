-- This script creates a trigger that decreases teh quentity of an item

DELIMITER $$

CREATE TRIGGER trg_after_insert_orders
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END$$

DELIMITER ;

