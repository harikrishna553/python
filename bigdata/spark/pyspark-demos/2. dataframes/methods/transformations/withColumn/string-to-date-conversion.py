from pyspark.sql import SparkSession
from pyspark.sql.functions import to_date
from pyspark.sql.types import StringType

# Initialize Spark session
spark = SparkSession.builder.appName("WithColumnToDateExample").getOrCreate()

# Sample data with dates stored as strings
data = [("Ram", "2000-02-15"), ("Krishna", "1989-08-10"), ("Chamu", "1995-12-05")]
df = spark.createDataFrame(data, ["Name", "DateOfBirth"])

# Convert string column to date format
df_converted = df.withColumn("DateOfBirth", to_date("DateOfBirth", "yyyy-MM-dd"))

# Show the original DataFrame
df.show()
df.printSchema()

# Show the transformed DataFrame
df_converted.show()
df_converted.printSchema()