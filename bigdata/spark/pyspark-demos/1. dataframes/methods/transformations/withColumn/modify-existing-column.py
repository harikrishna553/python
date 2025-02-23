from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit

# Create a Spark session
spark = (SparkSession.builder
         .appName("WithColumnExample")
         .getOrCreate())

# Sample DataFrame
data = [("Ram", 25), ("Krishna", 30), ("Chamu", 35)]
df = spark.createDataFrame(data, ["Name", "Age"])

# Increase age by 5 years
df_modified = df.withColumn("Age", col("Age") + 5)

# Show the results
df.show()
df_modified.show()
