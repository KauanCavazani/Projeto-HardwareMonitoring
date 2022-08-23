CREATE DATABASE hardwaremonitoring;
USE hardwareMonitoring;

CREATE TABLE users (
	idUser INT PRIMARY KEY AUTO_INCREMENT,
    nameUser VARCHAR(45),
    emailUser VARCHAR(45),
    passwdUser VARCHAR(45)
);

SELECT * FROM users;

drop table users;