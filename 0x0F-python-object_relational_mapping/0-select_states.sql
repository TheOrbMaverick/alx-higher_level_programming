-- Create states table in hbtn_0e_0_usa with some data
<<<<<<< HEAD
=======

>>>>>>> a6a66d15677b3710828151204004687b2827638a
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
<<<<<<< HEAD
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

=======
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");
>>>>>>> a6a66d15677b3710828151204004687b2827638a
