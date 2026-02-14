import pandas as pd

def extract_data(file_path: str) -> pd.DataFrame:
    """
    Extract data from CSV file using pandas
    """
    try:
        df = pd.read_csv(file_path)
        print("Data extraction successful.")
        print(f"Total records: {len(df)}")
        print("\nColumns:")
        print(df.columns.tolist())
        return df
    except Exception as e:
        print(f"Error during extraction: {e}")
        raise


if __name__ == "__main__":
    file_path = "data/SuperMarket Analysis.csv"
    df = extract_data(file_path)