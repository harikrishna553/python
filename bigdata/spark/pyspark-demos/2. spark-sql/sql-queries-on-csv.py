from pyspark.sql import SparkSession
from pyspark.sql import Row

# Create a SparkSession
spark = (SparkSession
         .builder
         .appName("SparkSQLExample")
         .getOrCreate())

# Convert to DataFrame
df = (spark
      .read
      .option("header", "true")
      .csv("data/employees.csv"))

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
