from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

# Initialize Spark Session
spark = SparkSession.builder.appName("SparkFileFormats").getOrCreate()

# Define Schema
schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("name", StringType(), True),
    StructField("age", IntegerType(), True)
])

# Create DataFrame
data = [(1, "Ram", 30), (2, "Krishna1", 25), (3, "Chamu", 35)]
df = spark.createDataFrame(data, schema)

# Show DataFrame
df.show()

df.write.mode("overwrite").json("data/employees_json")
