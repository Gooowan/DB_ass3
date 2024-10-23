CREATE USER 'admin_user'@'localhost' IDENTIFIED BY 'admin_password';
GRANT ALL PRIVILEGES ON Assignment3.* TO 'admin_user'@'localhost' WITH GRANT OPTION;


CREATE USER 'sel_user'@'localhost' IDENTIFIED BY 'sel_password';
GRANT SELECT ON Assignment3.* TO 'sel_user'@'localhost';

CREATE USER 'writer_user'@'localhost' IDENTIFIED BY 'write_password';
GRANT INSERT ON Assignment3.* TO 'writer_user'@'localhost';