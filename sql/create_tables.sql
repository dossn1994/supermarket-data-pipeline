-- Drop tables if they already exist
DROP TABLE IF EXISTS fact_sales;
DROP TABLE IF EXISTS dim_customer;
DROP TABLE IF EXISTS dim_product;

---------------------------------------------------
-- Dimension Table: Customer
---------------------------------------------------
CREATE TABLE dim_customer (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_type TEXT NOT NULL,
    gender TEXT NOT NULL,
    UNIQUE(customer_type, gender)
);

---------------------------------------------------
-- Dimension Table: Product
---------------------------------------------------
CREATE TABLE dim_product (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_line TEXT NOT NULL,
    unit_price REAL NOT NULL,
    UNIQUE(product_line, unit_price)
);

---------------------------------------------------
-- Fact Table: Sales
---------------------------------------------------
CREATE TABLE fact_sales (
    sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
    invoice_id TEXT,
    branch TEXT,
    city TEXT,
    date TEXT,
    time TEXT,
    payment TEXT,
    quantity INTEGER,
    tax REAL,
    sales REAL,
    cogs REAL,
    gross_income REAL,
    rating REAL,
    customer_id INTEGER,
    product_id INTEGER,
    
    FOREIGN KEY (customer_id) REFERENCES dim_customer(customer_id),
    FOREIGN KEY (product_id) REFERENCES dim_product(product_id)
);