# Inspiration: edX course "Building ETL and Data Pipelines with
# Bash, Airflow and Kafka".

from datetime import timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

# Defining DAG arguments

# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'me',
    'start_date': days_ago(0),
    'email': ['me@somemail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Defining the DAG
dag = DAG(
    'dummy_dag',
    default_args=default_args,
    description='My first DAG',
    schedule_interval=timedelta(minutes=1),
)

# Define the tasks

task1 = BashOperator(
    task_id='print_date',
    bash_command='date +%Y-%m-%d\ %H:%M:%S',
    dag=dag,
)

task2 = BashOperator(
    task_id='print_hello',
    bash_command='echo Hello World!',
    dag=dag,
)

task3 = BashOperator(
    task_id='sleep',
    bash_command='sleep 5',
    dag=dag,
)

# Task pipeline
task1 >> task2 >> task3
