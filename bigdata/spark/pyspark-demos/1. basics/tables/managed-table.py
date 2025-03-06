from pyspark.sql import SparkSession

# Step 1: Initialize SparkSession with Hive Support
spark = (SparkSession.builder
    .appName("ManagedTableDemo")
    .config("spark.sql.warehouse.dir", "/tmp/warehouse") 
    .getOrCreate())

# Step 2: Drop the table if it already exists (clean slate)
spark.sql("DROP TABLE IF EXISTS employees")

# Step 3: Create a Managed Table
spark.sql("""
    CREATE TABLE employees (
        id INT,
        name STRING,
        salary DOUBLE
    ) USING PARQUET
""")

# Step 4: Insert Sample Data
spark.sql("""
    INSERT INTO employees VALUES
    (1, 'Ram', 70000),
    (2, 'Krishna', 80000),
    (3, 'Chamu', 90000)
""")

# Step 5: Print Table Data
print("### Table Data ###")
spark.sql("SELECT * FROM employees").show()

# Step 6: Get Table Metadata (including storage location)
print("### Table Metadata ###")
metadata = spark.sql("DESCRIBE EXTENDED employees")
metadata.show(truncate=False)

# Step 7: Get the actual storage location of the table
table_location = spark.sql("DESCRIBE FORMATTED employees") \
    .filter("col_name = 'Location'") \
    .select("data_type").collect()[0][0]

print(f"Table Data Location: {table_location}")

print("Enter anything to proceed further")
input()

# Step 8: Drop the table (Deletes both metadata and data)
spark.sql("DROP TABLE employees")
print("Table dropped.")

# Step 9: Verify that the data is deleted
import os

if os.path.exists(table_location):
    print("Table data still exists! (Unexpected behavior)")
else:
    print("Table data deleted successfully.")

# Stop Spark Session
spark.stop()