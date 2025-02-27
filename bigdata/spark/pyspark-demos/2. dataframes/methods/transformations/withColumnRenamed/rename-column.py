from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

# Create Spark session
spark = (SparkSession.builder
         .appName("WithColumnRenamedExample")
         .getOrCreate())

# Sample Data
data = [(1, "Ram", 25), (2, "Krishna", 30), (3, "Chamu", 35)]

# Define Schema
schema = StructType([
    StructField("emp id", IntegerType(), True),
    StructField("emp name", StringType(), True),
    StructField("emp age", IntegerType(), True)
])

# Create DataFrame
df = spark.createDataFrame(data, schema)
df_renamed = df.withColumnRenamed("emp name", "employee_name")

df.show()
df_renamed.show()



