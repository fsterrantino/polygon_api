from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from airflow import DAG
import sys

sys.path.append('/opt/scripts/')
from poligon_api_request import make_request
from poligon_api_load import load_data

default_args={
    'owner': 'Fran',
    'retries':5,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    default_args=default_args,
    dag_id='Request_and_load',
    description= 'Prueba',
    start_date=datetime(2024,1,9),
    schedule_interval='0 0 * * *'
    ) as dag:

    task1 = PythonOperator(
        task_id='Request',
        python_callable=make_request,
        dag=dag,
    )

    task2 = PythonOperator(
        task_id='load_data',
        python_callable=load_data,
        dag=dag,
    )

task1
task2