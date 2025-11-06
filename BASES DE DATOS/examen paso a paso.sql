Iniciando sesión en MySQL
sudo mysql -u root -p

Creo la base de datos
CREATE DATABASE blog2;

Nos aseguramos de que se ha creado:
SHOW DATABASES;

Nos tenemos que meter en la base de datos:
USE blog2;

Creamos una tabla:
CREATE TABLE(
    Identificador INT(10),
    nombre VARCHAR(100),
    apellidos VARCHAR(100),
    email VARCHAR(100)
);

Comprobas si todo esta yendo bien comprobando con el siguiente comando las tablas:
SHOW TABLES;

Creamos una clave primaria
ALTER TABLE autores ADD COLUMN Identificador INT auto_increment PRIMARY KEY FIRST;

INSERT INTO autores VALUES(
    NULL,
    'Alex',
    'Sytnyk',
    'alex.sytnyk729@gmail.com'
);


