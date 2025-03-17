from airflow import DAG
from airflow.providers.mysql.hooks.mysql import MySqlHook
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd

# Define the default arguments
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 3, 14),
    'catchup': False
}

# Function to extract data from MySQL
def extract_data():
    mysql_hook = MySqlHook(mysql_conn_id='local_mysql_conn')
    sql = "SELECT * FROM employee"
    df = mysql_hook.get_pandas_df(sql)
    df.to_csv('/tmp/raw_employee_data.csv', index=False)
    print("Data extracted and saved as CSV.")

# Function to transform data
def transform_data():
    df = pd.read_csv('/tmp/raw_employee_data.csv')
    df_filtered = df[df['salary'] > 55000]  # Filter employees with salary > 55,000
    df_filtered.to_csv('/tmp/transformed_employee_data.csv', index=False)
    print("Data transformed and saved.")

# Define the DAG
with DAG('mysql_to_csv_pipeline', 
         default_args=default_args, 
         schedule_interval='@daily', 
         catchup=False) as dag:

    extract_task = PythonOperator(
        task_id='extract_data',
        python_callable=extract_data
    )

    transform_task = PythonOperator(
        task_id='transform_data',
        python_callable=transform_data
    )

    # Set task dependencies
    extract_task >> transform_task
