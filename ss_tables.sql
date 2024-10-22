CREATE TABLE Profile (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    shipping_address VARCHAR(255)
) COMMENT = 'Profile details associated with a user';

CREATE TABLE User (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    phone VARCHAR(15),
    profile_id INT,
    INDEX (username),
    CONSTRAINT fk_user_profile FOREIGN KEY (profile_id) REFERENCES Profile(id)
) COMMENT = 'Table for storing user details';

CREATE TABLE Category (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    description TEXT
) COMMENT = 'Table for product categories';

CREATE TABLE Product (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    category_id INT,
    remains INT,
    rating DECIMAL(3, 2),
    description TEXT,
    price DECIMAL(10, 2),
    CONSTRAINT fk_product_category FOREIGN KEY (category_id) REFERENCES Category(id),
    INDEX (name, category_id)
) COMMENT = 'Product details with linkage to categories';

CREATE TABLE `Order` (
    id INT AUTO_INCREMENT PRIMARY KEY,
    profile_id INT NOT NULL,
    total_cost DECIMAL(10, 2),
    created DATE,
    paid BOOLEAN,
    CONSTRAINT fk_order_profile FOREIGN KEY (profile_id) REFERENCES Profile(id),
    INDEX (profile_id)
) COMMENT = 'Orders placed by profiles';

CREATE TABLE Order_Product (
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    CONSTRAINT fk_orderproduct_order FOREIGN KEY (order_id) REFERENCES `Order`(id),
    CONSTRAINT fk_orderproduct_product FOREIGN KEY (product_id) REFERENCES Product(id),
    PRIMARY KEY (order_id, product_id),
    INDEX (order_id, product_id)
) COMMENT = 'Linking table for Orders and Products with quantities';

CREATE TABLE Liked_Products (
    profile_id INT,
    product_id INT,
    CONSTRAINT fk_liked_profile FOREIGN KEY (profile_id) REFERENCES Profile(id),
    CONSTRAINT fk_liked_product FOREIGN KEY (product_id) REFERENCES Product(id),
    PRIMARY KEY (profile_id, product_id),
    INDEX (profile_id, product_id)
) COMMENT = 'Table for storing profiles and their liked products';