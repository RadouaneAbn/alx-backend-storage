-- This script creates a table users

CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT,
    email varchar(255) NOT NULL,
    name varchar(255),
    PRIMARY KEY (id),
    UNIQUE (email)
);
