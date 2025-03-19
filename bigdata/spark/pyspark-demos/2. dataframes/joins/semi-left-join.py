from pyspark.sql import SparkSession

# Initialize Spark Session
spark = SparkSession.builder.appName("LeftSemiJoinExample").getOrCreate()

# Create Employees DataFrame
employees = [
    (1, "Ram", 10),
    (2, "Krishna", 20),
    (3, "Chamu", 30),
    (4, "Sailu", 40),
    (5, "Gopi", 50)
]

df1 = spark.createDataFrame(employees, ["id", "name", "dept_id"])

# Create Departments DataFrame
departments = [
    (10, "HR"),
    (20, "IT"),
    (30, "Finance")
]

df2 = spark.createDataFrame(departments, ["dept_id", "dept_name"])

# Perform Left Semi Join
result_df = df1.join(df2, "dept_id", "leftsemi")

# Show the result
result_df.show()
