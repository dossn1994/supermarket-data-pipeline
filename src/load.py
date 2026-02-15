def load_tables(conn, dim_customer_profile, dim_product, fact):
    """
    Load data into SQLite tables.
    """

    cursor = conn.cursor()

    # Execute table creation script
    with open("sql/create_tables.sql", "r") as f:
        cursor.executescript(f.read())

    # Insert data
    dim_customer_profile.to_sql(
        "dim_customer_profile",
        conn,
        if_exists="append",
        index=False
    )

    dim_product.to_sql(
        "dim_product",
        conn,
        if_exists="append",
        index=False
    )

    fact.to_sql(
        "fact_sales",
        conn,
        if_exists="append",
        index=False
    )

    # Execute indexes
    with open("sql/indexes.sql", "r") as f:
        cursor.executescript(f.read())

    conn.commit()