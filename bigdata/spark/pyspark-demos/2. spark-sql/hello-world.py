from pyspark.sql import SparkSession
from pyspark.sql import Row

# Create a SparkSession
spark = (SparkSession
         .builder
         .appName("SparkSQLExample")
         .getOrCreate())

# Sample Data
data = [
    Row(id=1, name="Ram", age=30, department="HR"),
    Row(id=2, name="Krishna", age=35, department="IT"),
    Row(id=3, name="Chamu", age=28, department="Finance"),
    Row(id=4, name="Sailu", age=40, department="IT"),
    Row(id=5, name="Gopi", age=45, department="HR")
]

# Convert to DataFrame
df = spark.createDataFrame(data)
df.show()

# Register the DataFrame as a Temporary SQL Table
df.createOrReplaceTempView("employees")

# Example 1: Select all data
print('Select all data')
result = spark.sql("SELECT * FROM employees")
result.show()

# Example 2: Get Employees Older Than 30
print('Get Employees Older Than 30')
result = spark.sql("SELECT name, age FROM employees WHERE age > 30")
result.show()

# Example 3: Count Employees by Department
print('Count Employees by Department')
result = spark.sql("SELECT department, COUNT(*) AS total FROM employees GROUP BY department")
result.show()
