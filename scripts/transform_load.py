import pandas as pd
import sqlite3


DATABASE_NAME = "supermarket.db"
CSV_PATH = "data/SuperMarket Analysis.csv"
SQL_SCHEMA_PATH = "sql/create_tables.sql"


def create_database():
    """
    Create SQLite database and tables
    """
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    with open(SQL_SCHEMA_PATH, "r") as f:
        schema_sql = f.read()

    cursor.executescript(schema_sql)
    conn.commit()
    print("Database and tables created successfully.")
    return conn


def load_dimensions(conn, df):
    """
    Load dimension tables
    """
    cursor = conn.cursor()

    # Load dim_customer
    customer_df = df[['Customer type', 'Gender']].drop_duplicates()

    for _, row in customer_df.iterrows():
        cursor.execute("""
            INSERT OR IGNORE INTO dim_customer (customer_type, gender)
            VALUES (?, ?)
        """, (row['Customer type'], row['Gender']))

    # Load dim_product
    product_df = df[['Product line', 'Unit price']].drop_duplicates()

    for _, row in product_df.iterrows():
        cursor.execute("""
            INSERT OR IGNORE INTO dim_product (product_line, unit_price)
            VALUES (?, ?)
        """, (row['Product line'], row['Unit price']))

    conn.commit()
    print("Dimension tables loaded successfully.")


def load_fact_table(conn, df):
    """
    Load fact table with foreign keys
    """
    cursor = conn.cursor()

    for _, row in df.iterrows():

        # Get customer_id
        cursor.execute("""
            SELECT customer_id FROM dim_customer
            WHERE customer_type = ? AND gender = ?
        """, (row['Customer type'], row['Gender']))
        customer_id = cursor.fetchone()[0]

        # Get product_id
        cursor.execute("""
            SELECT product_id FROM dim_product
            WHERE product_line = ? AND unit_price = ?
        """, (row['Product line'], row['Unit price']))
        product_id = cursor.fetchone()[0]

        # Insert into fact_sales
        cursor.execute("""
            INSERT INTO fact_sales (
                invoice_id, branch, city, date, time, payment,
                quantity, tax, sales, cogs, gross_income, rating,
                customer_id, product_id
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            row['Invoice ID'],
            row['Branch'],
            row['City'],
            row['Date'],
            row['Time'],
            row['Payment'],
            row['Quantity'],
            row['Tax 5%'],
            row['Sales'],
            row['cogs'],
            row['gross income'],
            row['Rating'],
            customer_id,
            product_id
        ))

    conn.commit()
    print("Fact table loaded successfully.")


def main():
    df = pd.read_csv(CSV_PATH)
    conn = create_database()
    load_dimensions(conn, df)
    load_fact_table(conn, df)
    conn.close()
    print("ETL process completed successfully.")


if __name__ == "__main__":
    main()