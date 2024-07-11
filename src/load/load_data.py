# load data into SQLAlchemy
import pathlib
import sqlite3
import pandas as pd


def create_table(db_dir: str, data: pd.DataFrame) -> None:

    conn = sqlite3.connect(db_dir)
    cursor = conn.cursor()

    # Create table (if it doesn't exist)
    create_table_query = """
        CREATE TABLE IF NOT EXISTS yellow_tripdata_2019_01 (
                VendorID INT,
                tpep_pickup_datetime DATETIME,
                tpep_dropoff_datetime DATETIME,
                passenger_count INT,
                trip_distance FLOAT,
                RatecodeID INT,
                store_and_fwd_flag VARCHAR(1),
                PULocationID INT,
                DOLocationID INT,
                payment_type INT,
                fare_amount FLOAT,
                extra FLOAT,
                mta_tax FLOAT,
                tip_amount FLOAT,
                tolls_amount FLOAT,
                improvement_surcharge FLOAT,
                total_amount FLOAT,
                trip_duration FLOAT,
                speed FLOAT,
                cost_per_mile FLOAT,
                cost_per_passanger FLOAT,
                tip_percent FLOAT
        )
    """
    cursor.execute(create_table_query)

    # Insert data from DataFrame into the SQLite table
    # yellow_tripdata_2019-01 - table name
    data.to_sql("yellow_tripdata_2019_01", conn, if_exists="append", index=False)

    conn.commit()
    conn.close()


if __name__ == "__main__":

    curr_dir = pathlib.Path(__file__)
    home_dir = curr_dir.parent.parent.parent.as_posix()
    db_dir = f"{home_dir}/database/sqlitedb.db"

    data_dir = f"{home_dir}/data/processed/yellow_processed_2019-01.csv"
    df = pd.read_csv(data_dir)

    try:
        create_table(db_dir, df)
        print("Data loaded into SQLite database successfully.")
    except Exception as e:
        print(f"Failed to load data into sqlitedb.\nError: {e}")
