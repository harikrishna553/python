from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

# Step 1: Initialize SparkSession
spark = SparkSession.builder.appName("DataFrameExample").getOrCreate()

# Step 2: Create a list of tuples (data)
data = [
    (1, "Krishna", 25),
    (2, "Ram", 30),
    (3, "Chamu", 28)
]

# Step 3: Define schema
schema = StructType([
    StructField("ID", IntegerType(), True),
    StructField("Name", StringType(), True),
    StructField("Age", IntegerType(), True)
])

# Step 4: Create DataFrame
df = spark.createDataFrame(data, schema=schema)

# Step 5: Show DataFrame
df.show()
