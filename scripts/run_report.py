import sqlite3
import pandas as pd


DATABASE_NAME = "supermarket.db"
REPORT_SQL_PATH = "sql/report.sql"


def run_report():
    """
    Execute analytical report query and display results
    """
    conn = sqlite3.connect(DATABASE_NAME)

    with open(REPORT_SQL_PATH, "r") as f:
        query = f.read()

    df = pd.read_sql_query(query, conn)

    print("\nAnalytical Report: Total Sales by Product Line\n")
    print(df)

    conn.close()


if __name__ == "__main__":
    run_report()