from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from airflow.providers.snowflake.hooks.snowflake import SnowflakeHook
from datetime import datetime
import pandas as pd
import os

DATA_PATH = "/opt/airflow/data"  # mount folder data di docker-compose

def export_snowflake_to_csv():
    hook = SnowflakeHook(snowflake_conn_id="snowflake_default")
    sql = "SELECT * FROM your_table LIMIT 100;"  # ganti sesuai kebutuhan
    df = hook.get_pandas_df(sql)
    
    # Simpan ke folder data
    os.makedirs(DATA_PATH, exist_ok=True)
    file_path = os.path.join(DATA_PATH, f"snowflake_export_{datetime.now().strftime('%Y%m%d')}.csv")
    df.to_csv(file_path, index=False)
    print(f"CSV saved to {file_path}")

default_args = {
    "owner": "airflow",
    "start_date": datetime(2025, 8, 1),
    "retries": 1,
}

with DAG(
    dag_id="snowflake_to_csv_dag",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False,
) as dag:

    export_task = PythonOperator(
        task_id="export_snowflake",
        python_callable=export_snowflake_to_csv,
    )
