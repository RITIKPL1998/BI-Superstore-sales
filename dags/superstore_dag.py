import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from scripts.transform import clean_data
from scripts.load_to_db import load_to_sqlite

default_args = {
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
}

with DAG(
    dag_id='superstore_etl_dag',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False
) as dag:

    transform_task = PythonOperator(
        task_id='transform_data',
        python_callable=clean_data
    )

    load_task = PythonOperator(
        task_id='load_data',
        python_callable=load_to_sqlite
    )

    transform_task >> load_task
