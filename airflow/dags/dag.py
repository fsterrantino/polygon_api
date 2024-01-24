from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from airflow import DAG
import sys

sys.path.append('/opt/scripts/')
from poligon_api_extract import extract_data
from poligon_api_transform import transform_data
from poligon_api_load import load_data
from poligon_api_alerts import alert_thresholds_gaps

default_args={
    'owner': 'Fran',
    'retries':5,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    default_args=default_args,
    dag_id='Polygon_API_ETL',
    description= 'Prueba',
    start_date=datetime(2024,1,22),
    # end_date=datetime(2024,1,19),
    schedule_interval='0 0 * * *'
    ) as dag:

    task1 = PythonOperator(
        task_id='extract_data',
        python_callable=extract_data,
        provide_context=True,
        depends_on_past=True,
        dag=dag
    )

    task2 = PythonOperator(
        task_id='transform_data',
        python_callable=transform_data,
        provide_context=True,
        dag=dag
    )

    task3 = PythonOperator(
        task_id='load_data',
        python_callable=load_data,
        provide_context=True,
        dag=dag
    )

    task4 = PythonOperator(
        task_id='alert_thresholds_gaps',
        python_callable=alert_thresholds_gaps,
        provide_context=True,
        dag=dag
    )

task1 >> task2 >> task3 >> task4