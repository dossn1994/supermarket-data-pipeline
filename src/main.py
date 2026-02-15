import yaml
from src.extract import extract_data
from src.validation import validate_dataframe
from src.transform import (
    create_dim_customer_profile,
    create_dim_product,
    create_fact
)
from src.database import get_connection
from src.load import load_tables
from src.logger import get_logger

logger = get_logger(__name__)

def main():

    with open("config/config.yaml") as f:
        config = yaml.safe_load(f)

    logger.info("Starting pipeline...")

    df = extract_data(
        config["dataset"],
        config["raw_data_path"]
    )

    validate_dataframe(df)

    dim_customer_profile = create_dim_customer_profile(df)
    dim_product = create_dim_product(df)
    fact = create_fact(
        df,
        dim_customer_profile,
        dim_product
    )

    conn = get_connection(config["database_path"])

    load_tables(
        conn,
        dim_customer_profile,
        dim_product,
        fact
    )

    logger.info("Pipeline completed successfully.")

if __name__ == "__main__":
    main()