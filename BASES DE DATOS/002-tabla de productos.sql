CREATE TABLE productos(
    nombre VARCHAR(255),
    precio DECIMAL(10,2),
    categoria VARCHAR(255),
    peso DECIMAL(10,2),
    stock INT,
    color VARCHAR(100)
);
INSERT INTO productos (nombre, precio, categoria, peso, stock, color) VALUES
('Manzana Roja', 1.20, 'Frutas', 0.15, 120, 'Rojo'),
('Manzana Verde', 1.10, 'Frutas', 0.14, 80, 'Verde'),
('Banana', 0.95, 'Frutas', 0.12, 200, 'Amarillo'),
('Pera Conferencia', 1.50, 'Frutas', 0.18, 60, 'Verde'),
('Naranja Valencia', 0.80, 'Frutas', 0.20, 300, 'Naranja'),

('Leche Entera 1L', 1.05, 'Lácteos', 1.00, 150, 'Blanco'),
('Leche Semidesnatada 1L', 1.00, 'Lácteos', 1.00, 140, 'Blanco'),
('Yogur Natural', 0.75, 'Lácteos', 0.12, 90, 'Blanco'),
('Queso Manchego', 12.50, 'Lácteos', 0.50, 30, 'Amarillo'),
('Mantequilla 250g', 2.20, 'Lácteos', 0.25, 50, 'Amarillo'),

('Pan de Barra', 0.90, 'Panadería', 0.25, 100, 'Marrón'),
('Croissant', 1.10, 'Panadería', 0.10, 70, 'Dorado'),
('Pan Integral', 1.40, 'Panadería', 0.35, 80, 'Marrón'),
('Donut Azúcar', 1.00, 'Panadería', 0.08, 50, 'Blanco'),
('Magdalena', 0.60, 'Panadería', 0.05, 90, 'Amarillo'),

('Agua Mineral 1.5L', 0.65, 'Bebidas', 1.50, 250, 'Transparente'),
('Coca-Cola 330ml', 1.20, 'Bebidas', 0.33, 180, 'Negro'),
('Cerveza Lager 330ml', 1.10, 'Bebidas', 0.33, 160, 'Dorado'),
('Vino Tinto Rioja', 6.80, 'Bebidas', 0.75, 40, 'Rojo'),
('Zumo de Naranja', 1.50, 'Bebidas', 1.00, 70, 'Naranja'),

('Arroz 1kg', 1.30, 'Alimentos Secos', 1.00, 150, 'Blanco'),
('Pasta Espagueti 500g', 1.10, 'Alimentos Secos', 0.50, 120, 'Amarillo'),
('Harina 1kg', 0.95, 'Alimentos Secos', 1.00, 100, 'Blanco'),
('Lentejas 1kg', 1.80, 'Alimentos Secos', 1.00, 80, 'Marrón'),
('Garbanzos 1kg', 1.90, 'Alimentos Secos', 1.00, 70, 'Beige'),

('Champú Aloe Vera', 3.90, 'Higiene', 0.30, 60, 'Verde'),
('Gel de Ducha', 2.50, 'Higiene', 0.40, 85, 'Azul'),
('Desodorante Spray', 2.20, 'Higiene', 0.20, 100, 'Blanco'),
('Pasta de Dientes', 1.80, 'Higiene', 0.10, 90, 'Blanco'),
('Crema Corporal', 4.50, 'Higiene', 0.25, 40, 'Rosa'),

('Camiseta Básica', 9.99, 'Ropa', 0.20, 40, 'Negro'),
('Pantalón Vaquero', 24.99, 'Ropa', 0.50, 25, 'Azul'),
('Sudadera Unisex', 19.90, 'Ropa', 0.40, 30, 'Gris'),
('Zapatillas Deportivas', 39.99, 'Ropa', 0.80, 20, 'Blanco'),
('Chaqueta Impermeable', 29.90, 'Ropa', 0.60, 15, 'Rojo'),

('Ratón Inalámbrico', 12.99, 'Electrónica', 0.09, 50, 'Negro'),
('Teclado Mecánico', 45.00, 'Electrónica', 0.70, 20, 'Negro'),
('Auriculares Bluetooth', 22.50, 'Electrónica', 0.15, 35, 'Blanco'),
('Powerbank 10000mAh', 18.90, 'Electrónica', 0.25, 30, 'Negro'),
('Monitor 24 pulgadas', 129.00, 'Electrónica', 3.50, 10, 'Negro');
