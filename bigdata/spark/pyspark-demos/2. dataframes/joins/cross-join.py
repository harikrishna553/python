from pyspark.sql import SparkSession

# Initialize Spark Session
spark = SparkSession.builder.appName("CrossJoinExample").getOrCreate()

# Create Employees DataFrame
employees = [
    (1, "Ram"),
    (2, "Krishna"),
    (3, "Chamu")
]

df1 = spark.createDataFrame(employees, ["id", "name"])

# Create Departments DataFrame
departments = [
    (10, "HR"),
    (20, "IT")
]

df2 = spark.createDataFrame(departments, ["dept_id", "dept_name"])

# Perform Cross Join
result_df = df1.crossJoin(df2)

# Show the result
result_df.show()
