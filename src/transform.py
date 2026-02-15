def create_dim_customer_profile(df):
    """
    Create customer profile dimension using surrogate key.
    """
    dim = (
        df[["Customer type", "Gender"]]
        .drop_duplicates()
        .reset_index(drop=True)
    )

    dim["customer_profile_id"] = dim.index + 1

    # Rename columns for warehouse clarity
    dim = dim.rename(columns={
        "Customer type": "customer_type",
        "Gender": "gender"
    })

    return dim


def create_dim_product(df):
    """
    Create product dimension using surrogate key.
    """
    dim = (
        df[["Product line"]]
        .drop_duplicates()
        .reset_index(drop=True)
    )

    dim["product_id"] = dim.index + 1

    dim = dim.rename(columns={
        "Product line": "product_line"
    })

    return dim


def create_fact(df, dim_customer_profile, dim_product):
    """
    Create fact_sales table.
    """

    df = df.merge(
        dim_customer_profile,
        left_on=["Customer type", "Gender"],
        right_on=["customer_type", "gender"]
    )

    df = df.merge(
        dim_product,
        left_on="Product line",
        right_on="product_line"
    )

    fact = df[[
        "Invoice ID",
        "customer_profile_id",
        "product_id",
        "Branch",
        "City",
        "Date",
        "Payment",
        "Quantity",
        "Unit price",
        "Sales",
        "gross income",
        "Rating"
    ]]

    fact = fact.rename(columns={
        "Invoice ID": "invoice_id",
        "Branch": "branch",
        "City": "city",
        "Date": "date",
        "Payment": "payment",
        "Quantity": "quantity",
        "Unit price": "unit_price",
        "Sales": "sales",
        "gross income": "gross_income",
        "Rating": "rating"
    })

    return fact