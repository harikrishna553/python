from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

# Initialize Spark Session
spark = SparkSession.builder.appName("SchemaExample").getOrCreate()

# Define Schema
schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("name", StringType(), True),
    StructField("age", IntegerType(), True)
])

# Create DataFrame with defined schema
data = [(1, "Ram", 25), (2, "Krishna", 30)]
df = spark.createDataFrame(data, schema=schema)

# Show DataFrame
df.show()
df.printSchema()