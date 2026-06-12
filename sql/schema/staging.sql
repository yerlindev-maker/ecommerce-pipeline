-- Creación del esquema de staging para datos crudos
CREATE SCHEMA IF NOT EXISTS staging;

-- Tabla para recibir los productos de la API
CREATE TABLE IF NOT EXISTS staging.products (
    id INT PRIMARY KEY,
    title TEXT,
    price NUMERIC,
    description TEXT,
    category TEXT,
    image TEXT,
    rating JSONB,
    extracted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
