from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, avg, count, max, min

# Initialize Spark session
spark = SparkSession.builder.appName("GroupingAggregations").getOrCreate()

# Sample data
data = [
    ("Ram", "Sales", 3000, "Bangalore"),
    ("Krishna", "Sales", 4000, "Chennai"),
    ("Chamu", "IT", 5000, "Bangalore"),
    ("Sailu", "IT", 6000, "Bangalore"),
    ("Jaideep", "IT", 9000, "Chennai"),
    ("Gopi", "HR", 4500, "Hyderabad"),
    ("Joel", "HR", 3500, "Hyderabad"),
    ("Raj", "HR", 5500, "Chennai"),
    ("Mukhar", "HR", 6500, "Chennai"),
]

# Define schema
columns = ["Employee", "Department", "Salary", "City"]

# Create DataFrame
df = spark.createDataFrame(data, columns)

# Show initial data
df.show()

# Grouping by a Department Column and Applying Multiple Aggregations
df.groupBy("Department").agg(
    sum("Salary").alias("Total_Salary"),
    avg("Salary").alias("Avg_Salary"),
    count("Employee").alias("Employee_Count")
).show()

# Grouping by a Department and City Columns and Applying Multiple Aggregations
df.groupBy("Department", "City").agg(
    max("Salary").alias("Max_Salary"),
    min("Salary").alias("Min_Salary")
).show()
