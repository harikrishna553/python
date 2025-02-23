from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Create a Spark session
spark = (SparkSession.builder
         .appName("CaseInsensitiveExample")
         .getOrCreate())

# Create a DataFrame with mixed-case column names
data = [(1, "Ram"), (2, "Krishna")]
df = spark.createDataFrame(data, ["ID", "Name"])

# Selecting columns using different cases
df.select("ID", "name").show()  # Works even though "name" was defined as "Name"
df.select(col("nAmE")).show()   # Also works
