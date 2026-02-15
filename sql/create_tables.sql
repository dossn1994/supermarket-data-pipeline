DROP TABLE IF EXISTS fact_sales;
DROP TABLE IF EXISTS dim_customer_profile;
DROP TABLE IF EXISTS dim_product;

CREATE TABLE dim_customer_profile (
    customer_profile_id INTEGER PRIMARY KEY,
    customer_type TEXT NOT NULL,
    gender TEXT NOT NULL
);

CREATE TABLE dim_product (
    product_id INTEGER PRIMARY KEY,
    product_line TEXT NOT NULL
);

CREATE TABLE fact_sales (
    sales_id INTEGER PRIMARY KEY AUTOINCREMENT,
    invoice_id TEXT NOT NULL,
    customer_profile_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    branch TEXT,
    city TEXT,
    date TEXT,
    payment TEXT,
    quantity INTEGER,
    unit_price REAL,
    sales REAL,
    gross_income REAL,
    rating REAL,
    FOREIGN KEY (customer_profile_id)
        REFERENCES dim_customer_profile(customer_profile_id),
    FOREIGN KEY (product_id)
        REFERENCES dim_product(product_id)
);