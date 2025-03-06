from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("SparkExample").getOrCreate()

# Sample Employee Data
columns = ["ID", "Name", "Age", "Department", "Salary"]
data = [
    (1, "Ram", 30, "HR", 50000),
    (2, "Krishna", 25, "IT", 60000),
    (3, "Chamu", 35, "Finance", 70000),
    (4, "Sailu", 40, "IT", 80000)
]

df = spark.createDataFrame(data, schema=columns)

# Register DataFrame as a temporary SQL table
df.createOrReplaceTempView("employees")

# Execute SQL query to find IT department employees
sql_result = spark.sql("SELECT Name FROM employees WHERE Department = 'IT'")
sql_result.show()
