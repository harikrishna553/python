from pyspark.sql import SparkSession
from pyspark.sql import Row

# Initialize Spark Session
spark = SparkSession.builder.appName("DropDuplicatesExample").getOrCreate()

# Sample Data
data = [
    Row(id=1, name="Ram", age=25),
    Row(id=2, name="Krishna", age=30),
    Row(id=1, name="Ram", age=25),  # Duplicate row based on name
    Row(id=3, name="Chamu", age=35),
    Row(id=1, name="Ram", age=35),  # Duplicate row based on name
]

df = spark.createDataFrame(data)
print("Original DataFrame:")
df.show()

# Dropping duplicates based on the 'name' column
df_unique_names = df.dropDuplicates(["name"])

print("DataFrame after dropping duplicates based on 'name':")
df_unique_names.show()
