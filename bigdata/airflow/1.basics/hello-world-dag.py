from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# Define Python functions for tasks
def task_1():
    print("Task 1: Start of workflow")

def task_2():
    print("Task 2: Running in parallel with Task 3")

def task_3():
    print("Task 3: Running in parallel with Task 2")

def task_4():
    print("Task 4: Runs after Task 2 and Task 3")

# Define DAG
dag = DAG(
    'my_dag',
    schedule_interval='@daily',
    start_date=datetime(2024, 1, 1),
    catchup=False
)

# Define tasks
start_task = PythonOperator(
    task_id='start_workflow',
    python_callable=task_1,
    dag=dag
)

parallel_task_1 = PythonOperator(
    task_id='parallel_task_1',
    python_callable=task_2,
    dag=dag
)

parallel_task_2 = PythonOperator(
    task_id='parallel_task_2',
    python_callable=task_3,
    dag=dag
)

final_task = PythonOperator(
    task_id='final_task',
    python_callable=task_4,
    dag=dag
)

# Define dependencies
start_task >> [parallel_task_1, parallel_task_2]  # Run Task 2 and Task 3 in parallel
[parallel_task_1, parallel_task_2] >> final_task  # Run Task 4 after Task 2 & Task 3
