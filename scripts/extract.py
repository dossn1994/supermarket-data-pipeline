import os
from kaggle.api.kaggle_api_extended import KaggleApi


def download_data():
    """
    Downloads the Supermarket Sales dataset from Kaggle
    and stores it inside the data/ folder.
    """

    os.makedirs("data", exist_ok=True)

    api = KaggleApi()
    api.authenticate()

    api.dataset_download_files(
        "faresashraf1001/supermarket-sales",
        path="data",
        unzip=True
    )

    print("Data downloaded successfully from Kaggle.")


if __name__ == "__main__":
    download_data()
