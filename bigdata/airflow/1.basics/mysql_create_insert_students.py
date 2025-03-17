from airflow import DAG
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from datetime import datetime

# Default arguments for the DAG
default_args = {
    "owner": "airflow",
    "start_date": datetime(2024, 3, 14),  # DAG will not run before this date
}

# Define the DAG
with DAG(
    dag_id="mysql_create_insert_students",
    default_args=default_args,
    schedule_interval="@once",  # Run only once manually
    catchup=False  # Ensure no backfilling of past runs
) as dag:

    # Task 1: Create 'students' table
    create_students_table = SQLExecuteQueryOperator(
        task_id="create_students_table",
        conn_id="local_mysql_conn",  # Using the pre-configured MySQL connection
        sql="""
        CREATE TABLE IF NOT EXISTS students (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            age INT NOT NULL,
            grade VARCHAR(10) NOT NULL
        );
        """
    )

    # Task 2: Insert sample data
    insert_students_data = SQLExecuteQueryOperator(
        task_id="insert_students_data",
        conn_id="local_mysql_conn",
        sql="""
        INSERT INTO students (name, age, grade) VALUES 
        ('Ram', 14, '8th'),
        ('Krishna', 15, '9th'),
        ('Chamu', 13, '7th');
        """
    )

    # Define task execution order
    create_students_table >> insert_students_data
