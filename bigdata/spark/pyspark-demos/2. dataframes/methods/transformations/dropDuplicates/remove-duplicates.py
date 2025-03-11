from pyspark.sql import SparkSession
from pyspark.sql import Row

# Initialize Spark Session
spark = SparkSession.builder.appName("DropDuplicatesExample").getOrCreate()

# Sample Data
data = [
    Row(id=1, name="Ram", age=25),
    Row(id=2, name="Krishna", age=30),
    Row(id=1, name="Ram", age=25),  # Duplicate row
    Row(id=3, name="Chamu", age=35)
]

df = spark.createDataFrame(data)
print("Original DataFrame:")
df.show()

# Dropping complete duplicate rows
df_no_duplicates = df.dropDuplicates()

print("DataFrame after dropDuplicates:")
df_no_duplicates.show()
