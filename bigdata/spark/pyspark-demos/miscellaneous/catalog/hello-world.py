from pyspark.sql import SparkSession

def create_spark_session(app_name="CatalogExample", warehouse_dir="/tmp/spark-warehouse"):
    """
    Creates and returns a Spark session.
    """
    spark = (SparkSession.builder
             .appName(app_name)
             .config("spark.sql.warehouse.dir", warehouse_dir)
             .enableHiveSupport()  # Enables Hive support for database operations
             .getOrCreate())
    return spark

def create_tables(spark, db_name, tables):
    """
    Creates a database and its tables with given schemas.

    Parameters:
        spark (SparkSession): Active Spark session.
        db_name (str): Name of the database.
        tables (dict): Dictionary of table names as keys and column definitions as values.
    """
    spark.sql(f"CREATE DATABASE IF NOT EXISTS {db_name}")
    print(f"Database '{db_name}' created.")

    spark.sql(f"USE {db_name}")  # Switch to the database
    for table_name, table_schema in tables.items():
        spark.sql(f"CREATE TABLE IF NOT EXISTS {table_name} ({table_schema})")
        print(f"Table '{table_name}' created in '{db_name}'.")

def insert_sample_data(spark, db_name, table_data):
    """
    Inserts sample data into the given tables.

    Parameters:
        spark (SparkSession): Active Spark session.
        db_name (str): Name of the database.
        table_data (dict): Dictionary where keys are table names and values are lists of row tuples.
    """
    spark.sql(f"USE {db_name}")
    for table_name, rows in table_data.items():
        for row in rows:
            values = ", ".join(f"'{v}'" if isinstance(v, str) else str(v) for v in row)
            spark.sql(f"INSERT INTO {table_name} VALUES ({values})")
        print(f"Inserted {len(rows)} rows into '{table_name}' in '{db_name}'.")

def fetch_and_print_data(spark, db_name, tables):
    """
    Fetches and prints data from the given tables.

    Parameters:
        spark (SparkSession): Active Spark session.
        db_name (str): Name of the database.
        tables (list): List of table names to retrieve data from.
    """
    spark.sql(f"USE {db_name}")
    for table in tables:
        print(f"\nData from '{db_name}.{table}':")
        spark.sql(f"SELECT * FROM {table}").show()

def explore_catalog(spark):
    """
    Uses spark.catalog to explore databases, tables, and columns.
    """
    print("\n### Listing Databases ###")
    databases = spark.catalog.listDatabases()
    for db in databases:
        print(f"- {db.name}")

    for db in databases:
        print(f"\n### Tables in Database: {db.name} ###")
        tables = spark.catalog.listTables(db.name)
        for table in tables:
            print(f"- {table.name} (Type: {table.tableType})")

            print(f"  Columns in Table '{table.name}':")
            columns = spark.catalog.listColumns(table.name, db.name)
            for column in columns:
                print(f"    - {column.name} ({column.dataType})")

# Main Execution
if __name__ == "__main__":
    spark = create_spark_session()

    # Define databases, tables, and sample data
    databases = {
        "sales_db": {
            "sales": "id INT, amount DOUBLE",
            "transactions": "txn_id INT, customer_id INT, txn_amount DOUBLE"
        },
        "hr_db": {
            "employees": "id INT, name STRING, salary DOUBLE",
            "departments": "dept_id INT, dept_name STRING"
        }
    }

    sample_data = {
        "sales_db": {
            "sales": [(1, 100.50), (2, 200.75)],
            "transactions": [(101, 1, 100.50), (102, 2, 200.75)]
        },
        "hr_db": {
            "employees": [(1, "Alice", 50000), (2, "Bob", 60000)],
            "departments": [(1, "HR"), (2, "Engineering")]
        }
    }

    # Create databases and tables
    for db_name, tables in databases.items():
        create_tables(spark, db_name, tables)

    # Insert sample data
    for db_name, table_data in sample_data.items():
        insert_sample_data(spark, db_name, table_data)

    # Fetch and print data
    for db_name, tables in databases.items():
        fetch_and_print_data(spark, db_name, list(tables.keys()))

    # Explore catalog metadata
    explore_catalog(spark)

    # Stop Spark session
    spark.stop()
