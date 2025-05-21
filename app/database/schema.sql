-- Create Scripts

CREATE TABLE IF NOT EXISTS products (
    id BIGSERIAL PRIMARY KEY,
    name TEXT UNIQUE NOT NULL,
    description TEXT,
    price NUMERIC(10,2)
);

-- Optional: insert sample data
INSERT INTO products (name, description, price) VALUES
('iPhone 13 Pro', 'Apple smartphone with A15 chip', 999.99),
('Samsung Galaxy S21', 'Samsung flagship phone with AMOLED display', 849.50)
ON CONFLICT (name) DO NOTHING;