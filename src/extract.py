from kaggle.api.kaggle_api_extended import KaggleApi
import pandas as pd
import os
from src.logger import get_logger

logger = get_logger(__name__)


def extract_data(dataset: str, raw_path: str) -> pd.DataFrame:
    """
    Downloads dataset from Kaggle and returns dataframe.
    """

    try:
        logger.info("Authenticating Kaggle API...")
        api = KaggleApi()
        api.authenticate()

        logger.info("Downloading dataset from Kaggle...")
        api.dataset_download_files(dataset, path=raw_path, unzip=True)

        # After unzip, Kaggle dataset file name:
        # It usually comes as "supermarket_sales.csv"
        files = os.listdir(raw_path)

        csv_files = [f for f in files if f.endswith(".csv")]

        if not csv_files:
            raise FileNotFoundError("No CSV file found in raw data path")

        file_path = os.path.join(raw_path, csv_files[0])

        logger.info(f"Reading file: {file_path}")

        df = pd.read_csv(file_path)

        logger.info("Extraction completed successfully.")

        return df

    except Exception as e:
        logger.exception("Extraction failed.")
        raise