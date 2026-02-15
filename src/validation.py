def validate_dataframe(df):
    """
    Perform structural and basic data quality validation.
    """

    if df.empty:
        raise ValueError("Dataframe is empty")

    required_columns = [
        "Invoice ID",
        "Customer type",
        "Gender",
        "Product line",
        "Sales",
        "Quantity",
        "Rating"
    ]

    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")

    # Null checks
    if df["Invoice ID"].isnull().any():
        raise ValueError("Null values found in Invoice ID")

    if df["Sales"].isnull().any():
        raise ValueError("Null values found in Sales")

    # Uniqueness check
    if not df["Invoice ID"].is_unique:
        raise ValueError("Invoice ID is not unique")

    # Business rule checks
    if (df["Sales"] <= 0).any():
        raise ValueError("Invalid Sales values detected")

    if (df["Quantity"] <= 0).any():
        raise ValueError("Invalid Quantity values detected")

    if not df["Rating"].between(0, 10).all():
        raise ValueError("Invalid Rating values detected")