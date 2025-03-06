from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

# Initialize Spark Session
spark = SparkSession.builder.appName("SchemaExample").getOrCreate()

# Define Schema using DDL String
ddl_schema = "id INT, name STRING, age INT"

# Create DataFrame with defined schema
data = [(1, "Ram", 25), (2, "Krishna", 30)]
df = spark.createDataFrame(data, schema=ddl_schema)

# Show DataFrame
df.show()
df.printSchema()