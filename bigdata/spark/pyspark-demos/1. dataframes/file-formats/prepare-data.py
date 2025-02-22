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
data = [(1, "Ram", 30), (2, "Krishna", 25), (3, "Chamu", 35)]
df = spark.createDataFrame(data, schema)

# Show DataFrame
df.show()

df.write.mode("overwrite").json("data/employees_json")
df.write.mode("overwrite").csv("data/employees_csv", header=True)
df.write.mode("overwrite").parquet("data/employees_parquet")
df.write.mode("overwrite").orc("data/employees_orc")
df.selectExpr("to_json(struct(*)) as value").write.mode("overwrite").text("data/employees_text")
