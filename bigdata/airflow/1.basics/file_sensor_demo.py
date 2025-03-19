from airflow import DAG
from airflow.sensors.filesystem import FileSensor
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

# Define default arguments
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2024, 3, 19),
    "retries": 1,
    "retry_delay": timedelta(minutes=2),
}

# Function to log DAG start
def log_start():
    print("DAG execution started. Waiting for the file...")

# Function to log file detection
def log_file_found():
    print("File detected! Proceeding to process the file...")

# Function to simulate file processing
def process_file():
    print("Processing the file now...")

# Define the DAG
dag = DAG(
    "file_sensor_example",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False,
)

# Task 1: Log start of DAG execution
start_task = PythonOperator(
    task_id="log_start",
    python_callable=log_start,
    dag=dag,
)

# Task 2: FileSensor - Wait for the file
wait_for_file = FileSensor(
    task_id="wait_for_orders_file",
    filepath="/tmp/data/orders.csv",
    fs_conn_id="fs_default",  # Airflow connection for filesystem
    poke_interval=30,  # Check every 30 seconds
    timeout=600,  # Timeout after 10 minutes
    mode="poke",  # Use "poke" mode (default) or "reschedule"
    dag=dag,
)

# Task 3: Log file detection
file_found_task = PythonOperator(
    task_id="log_file_found",
    python_callable=log_file_found,
    dag=dag,
)

# Task 4: Process file
process_file_task = PythonOperator(
    task_id="process_file",
    python_callable=process_file,
    dag=dag,
)

# Define Task Order
start_task >> wait_for_file >> file_found_task >> process_file_task
