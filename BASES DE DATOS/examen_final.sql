-- Crear la base de datos
CREATE DATABASE portafolioexamen;
USE portafolioexamen;

-- Crear tabla de categorías
CREATE TABLE categoriasportafolio (
    Identificador INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

-- Crear tabla de piezas
CREATE TABLE piezasportafolio (
    Identificador INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(150) NOT NULL,
    descripcion TEXT,
    fecha DATE,
    id_categoria INT,
    FOREIGN KEY (id_categoria) REFERENCES categoriasportafolio(Identificador)
);


---------------SEGUNDA PARTE DEL EJERCICIO---------------
INSERT INTO categoriasportafolio (nombre)
VALUES ('Diseño web'), ('Fotográfia'), ('Programación');

--Inserto registros en piezas--
INSERT INTO piezasportafolio (titulo, descripcion, fecha, id_categoria)
VALUES ('Pagina personal', 'Sitio web desarollado en HTML y CSS', '2021-05-10', 1),
('Rertato urbano', 'Fotografia en exteriores', '2022-07-25', 2),
('Arte digital', 'Ilustracion creada con tableta grafica', '2023-02-19', 3);

--Lectura de todos los registros--
SELECT * FROM piezasportafolio;

--Actualización de un registro--
UPDATE piezasportafolio
SET titulo = 'Portafolio Personal Actualizado'
WHERE Identificador = 1;

--Eliminacion de un registro--
DELETE FROM piezasportafolio
WHERE Identificador = 3;

--Consulta con el LEFT JOIN--
SELECT
p.Identificador,
p.titulo,
p.descripcion,
p.fecha,
c.nombre AS categoria
FROM piezasportafolio p
LEFT JOIN categoriasportafolio c
ON p.id_categoria = c.Identificador;

--Creacion de una vista basada en el LEFT JION--
CREATE VIEW vista_portafolio AS
SELECT 
p.Identificador,
p.titulo,
p.descripcion,
p.fecha,
c.nombre AS categoria
FROM piezasportafolio p
LEFT JOIN categoriasportafolio c
ON p.id_categoria = c.Identificador;

--Consulta para visualizar la vista--
SELECT * FROM vista_portafolio;

