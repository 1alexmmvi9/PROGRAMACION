-- PASO 1: Crear la base de datos y usarla
CREATE DATABASE biblioteca25;
USE biblioteca25;

-- Verifico
SELECT DATABASE();

+----------------+
| DATABASE()     |
+----------------+
| biblioteca25   |
+----------------+


-- PASO 2: Crear tabla autores
CREATE TABLE autores (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(100),
  pais VARCHAR(80)
);

-- Verifico
DESCRIBE autores;

+--------+--------------+------+-----+---------+----------------+
| Field  | Type         | Null | Key | Default | Extra          |
+--------+--------------+------+-----+---------+----------------+
| id     | int          | NO   | PRI | NULL    | auto_increment |
| nombre | varchar(100) | YES  |     | NULL    |                |
| pais   | varchar(80)  | YES  |     | NULL    |                |
+--------+--------------+------+-----+---------+----------------+


-- PASO 3: Crear tabla libros
CREATE TABLE libros (
  id INT AUTO_INCREMENT PRIMARY KEY,
  titulo VARCHAR(200),
  isbn VARCHAR(20),
  precio DECIMAL(8,2),
  autor_id INT,
  FOREIGN KEY (autor_id) REFERENCES autores(id)
);

-- Verifico
DESCRIBE libros;

+----------+---------------+------+-----+---------+----------------+
| Field    | Type          | Null | Key | Default | Extra          |
+----------+---------------+------+-----+---------+----------------+
| id       | int           | NO   | PRI | NULL    | auto_increment |
| titulo   | varchar(200)  | YES  |     | NULL    |                |
| isbn     | varchar(20)   | YES  |     | NULL    |                |
| precio   | decimal(8,2)  | YES  |     | NULL    |                |
| autor_id | int           | YES  | MUL | NULL    |                |
+----------+---------------+------+-----+---------+----------------+


-- PASO 4: Crear tabla socios
CREATE TABLE socios (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(100),
  email VARCHAR(120),
  fecha_alta DATE
);

-- Verifico
DESCRIBE socios;

+------------+--------------+------+-----+---------+----------------+
| Field      | Type         | Null | Key | Default | Extra          |
+------------+--------------+------+-----+---------+----------------+
| id         | int          | NO   | PRI | NULL    | auto_increment |
| nombre     | varchar(100) | YES  |     | NULL    |                |
| email      | varchar(120) | YES  |     | NULL    |                |
| fecha_alta | date         | YES  |     | NULL    |                |
+------------+--------------+------+-----+---------+----------------+


-- PASO 5: Crear tabla prestamos
CREATE TABLE prestamos (
  id INT AUTO_INCREMENT PRIMARY KEY,
  socio_id INT,
  libro_id INT,
  fecha_prestamo DATE,
  fecha_devolucion DATE,
  FOREIGN KEY (socio_id) REFERENCES socios(id),
  FOREIGN KEY (libro_id) REFERENCES libros(id)
);

-- Verifico
DESCRIBE prestamos;

+-----------------+------+-----+---------+----------------+
| Field           | Type | Null | Key | Default | Extra  |
+-----------------+------+-----+---------+----------------+
| id              | int  | NO   | PRI | NULL    | auto_increment |
| socio_id        | int  | YES  | MUL | NULL    |                |
| libro_id        | int  | YES  | MUL | NULL    |                |
| fecha_prestamo  | date | YES  |     | NULL    |                |
| fecha_devolucion| date | YES  |     | NULL    |                |
+-----------------+------+-----+---------+----------------+


-- PASO 6: Insertar datos de ejemplo

-- Autores
INSERT INTO autores (nombre, pais) VALUES
('Isabel Allende', 'Chile'),
('Gabriel García Márquez', 'Colombia'),
('Haruki Murakami', 'Japón');

-- Libros
INSERT INTO libros (titulo, isbn, precio, autor_id) VALUES
('La casa de los espíritus', '9788401352836', 18.50, 1),
('Cien años de soledad', '9780307474728', 22.00, 2),
('Kafka en la orilla', '9788499082478', 17.00, 3);

-- Socios
INSERT INTO socios (nombre, email, fecha_alta) VALUES
('Ana Ruiz', 'ana.ruiz@example.com', '2025-10-01'),
('Luis Pérez', 'luis.perez@example.com', '2025-10-10');

-- Préstamos
INSERT INTO prestamos (socio_id, libro_id, fecha_prestamo, fecha_devolucion) VALUES
(1, 1, '2025-10-25', NULL),
(2, 2, '2025-10-20', '2025-10-28');


-- PASO 7: Verifico si las tablas tienen datos, bueno, y muestro a la vez como se ven en el codigo

SELECT * FROM autores;

+----+-----------------------+-----------+
| id | nombre                | pais      |
+----+-----------------------+-----------+
| 1  | Isabel Allende        | Chile     |
| 2  | Gabriel García Márquez| Colombia  |
| 3  | Haruki Murakami       | Japón     |
+----+-----------------------+-----------+


SELECT * FROM libros;

+----+--------------------------+-------------+--------+----------+
| id | titulo                   | isbn        | precio | autor_id |
+----+--------------------------+-------------+--------+----------+
| 1  | La casa de los espíritus | 9788401352836 | 18.50 | 1        |
| 2  | Cien años de soledad     | 9780307474728 | 22.00 | 2        |
| 3  | Kafka en la orilla       | 9788499082478 | 17.00 | 3        |
+----+--------------------------+-------------+--------+----------+


SELECT * FROM socios;

+----+-----------+-----------------------+-------------+
| id | nombre    | email                 | fecha_alta  |
+----+-----------+-----------------------+-------------+
| 1  | Ana Ruiz  | ana.ruiz@example.com  | 2025-10-01  |
| 2  | Luis Pérez| luis.perez@example.com| 2025-10-10  |
+----+-----------+-----------------------+-------------+


SELECT * FROM prestamos;

+----+----------+----------+---------------+-----------------+
| id | socio_id | libro_id | fecha_prestamo| fecha_devolucion|
+----+----------+----------+---------------+-----------------+
| 1  | 1        | 1        | 2025-10-25    | NULL            |
| 2  | 2        | 2        | 2025-10-20    | 2025-10-28      |
+----+----------+----------+---------------+-----------------+


-- PASO FINAL: Verifico todas las tablas
SHOW TABLES;

+----------------+
| Tables_in_biblioteca25 |
+----------------+
| autores        |
| libros         |
| socios         |
| prestamos      |
+----------------+

DESCRIBE autores;
DESCRIBE libros;
DESCRIBE socios;
DESCRIBE prestamos;

