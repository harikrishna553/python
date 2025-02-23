from pyspark.sql import SparkSession
from pyspark.sql.functions import to_timestamp

# Initialize Spark session
spark = SparkSession.builder.appName("WithColumnToTimestampExample").getOrCreate()

# Sample data with timestamps stored as strings
data = [("Ram", "2024-02-15 14:30:00"), ("Krishna", "2023-08-10 09:15:00")]
df = spark.createDataFrame(data, ["Name", "EventTime"])

# Convert string column to timestamp format
df_converted = df.withColumn("EventTime", to_timestamp("EventTime", "yyyy-MM-dd HH:mm:ss"))

# Show the original DataFrame
df.show()
df.printSchema()

# Show the transformed DataFrame
df_converted.show()
df_converted.printSchema()
