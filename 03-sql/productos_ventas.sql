-- 1. TABLA DE PRODUCTOS.
CREATE TABLE productos (
    id_producto INT PRIMARY KEY,
    nombre VARCHAR(50),
    categoria VARCHAR(30),
    precio DECIMAL(10, 2),
    stock INT
);

-- 2. TABLA DE VENTAS (Relacionada con productos mediante id_producto).
CREATE TABLE ventas (
    id_venta INT PRIMARY KEY,
    id_producto INT,
    cantidad INT,
    fecha DATE,
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
);
