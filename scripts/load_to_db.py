import pandas as pd
import sqlite3
import os

def load_to_sqlite():
    input_path = '/opt/airflow/data/processed/cleaned_data.csv'
    db_path = '/opt/airflow/db/superstore.db'

    df = pd.read_csv(input_path)
    os.makedirs(os.path.dirname(db_path), exist_ok=True)

    conn = sqlite3.connect(db_path)
    df.to_sql('orders', conn, if_exists='replace', index=False)
    conn.close()
