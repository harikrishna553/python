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
new_column_names = ["employee_id", "employee_name", "employee_age"]
df_renamed =  df.toDF(*new_column_names)

df.show()
df_renamed.show()



