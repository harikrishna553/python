from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, TimestampType
from pyspark.sql.functions import to_timestamp

# Initialize Spark Session
spark = SparkSession.builder.appName("LogParser").getOrCreate()

# Read log file as RDD
log_rdd = spark.sparkContext.textFile("logs.txt")

# Split log lines into structured fields
log_rdd = log_rdd.map(lambda line: line.split(" ", 3)) \
                 .map(lambda parts: (f"{parts[0]} {parts[1]}", parts[2], parts[3].split(":")[0], parts[3].split(": ", 1)[1]))

# Define schema with TimestampType
schema = StructType([
    StructField("timestamp", StringType(), True),  # Initially, keep it as StringType for conversion
    StructField("logLevel", StringType(), True),
    StructField("className", StringType(), True),
    StructField("message", StringType(), True)
])

# Convert RDD to DataFrame using the schema
log_df = spark.createDataFrame(log_rdd, schema=schema)

# Convert timestamp column from string to TimestampType using Spark's built-in function
log_df = log_df.withColumn("timestamp", to_timestamp(log_df["timestamp"], "dd/MM/yy HH:mm:ss"))

# Show parsed logs
log_df.show(truncate=False)

# Print Schema to verify timestamp type
log_df.printSchema()

# Stop Spark Session
spark.stop()
