from pyspark.sql import SparkSession
from pyspark.sql import Row

# Initialize Spark Session
spark = SparkSession.builder.appName("DropColumnsExample").getOrCreate()

# Sample data
data = [
    Row(id=1, name="Ram", age=30, department="HR"),
    Row(id=2, name="Krishna", age=35, department="Finance"),
    Row(id=3, name="Sailu", age=40, department="IT")
]

# Create DataFrame
df = spark.createDataFrame(data)
print("Original DataFrame:")
df.show()

# Drop the 'age' and 'department' columns
df_dropped = df.drop("age", "department")
print("DataFrame after dropping 'age' and 'department':")
df_dropped.show()
