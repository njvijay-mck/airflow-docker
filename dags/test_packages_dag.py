from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import pandas as pd
import numpy as np

def test_packages():
    print(f"pandas version: {pd.__version__}")
    print(f"numpy version: {np.__version__}")

with DAG('test_packages_dag', start_date=datetime(2023, 1, 1), schedule_interval=timedelta(days=1)) as dag:
    PythonOperator(
        task_id='test_packages_task',
        python_callable=test_packages
    )