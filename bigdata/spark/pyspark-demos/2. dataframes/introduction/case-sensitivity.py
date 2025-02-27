from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Create a Spark session
spark = (SparkSession.builder
         .appName("CaseInsensitiveExample")
         .getOrCreate())

spark.conf.set("spark.sql.caseSensitive", "true")

# Create a DataFrame with mixed-case column names
data = [(1, "Ram"), (2, "Krishna")]
df = spark.createDataFrame(data, ["ID", "Name"])

# Selecting columns using different cases
df.select(col("Name")).show()   # This works
df.select(col("name")).show()   # This not works