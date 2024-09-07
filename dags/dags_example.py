from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

# Define default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 9, 5),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
dag = DAG(
    'Vijay_example_python_bash_dag',
    default_args=default_args,
    description='A simple DAG with Python and Bash tasks',
    schedule_interval=timedelta(days=1),
)

# Python function to be executed
def print_hello():
    return 'Hello from Python!'

# Define tasks
t1 = PythonOperator(
    task_id='print_hello',
    python_callable=print_hello,
    dag=dag,
)

t2 = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=dag,
)

t3 = BashOperator(
    task_id='sleep',
    bash_command='sleep 5',
    dag=dag,
)

t4 = BashOperator(
    task_id='print_end',
    bash_command='echo "DAG has finished!"',
    dag=dag,
)

# Set task dependencies
# t1 runs first, then t2 and t3 in parallel, finally t4
t1 >> [t2, t3] >> t4