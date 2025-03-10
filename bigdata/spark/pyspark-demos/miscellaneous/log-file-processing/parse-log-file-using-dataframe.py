from pyspark.sql import SparkSession
from pyspark.sql.functions import split, concat_ws, to_timestamp

# Initialize Spark Session
spark = SparkSession.builder.appName("LogParser").getOrCreate()

# Read the log file into a DataFrame (each line as a single column)
log_df = spark.read.text("logs.txt")

# Split the log lines into structured columns
log_df = log_df.withColumn("date_part", split(log_df["value"], " ")[0]) \
               .withColumn("time_part", split(log_df["value"], " ")[1]) \
               .withColumn("logLevel", split(log_df["value"], " ")[2]) \
               .withColumn("className", split(split(log_df["value"], " ", 4)[3], ":")[0]) \
               .withColumn("message", split(log_df["value"], ": ", 2)[1]) \
               .drop("value")

# Combine date and time before converting to TimestampType
log_df = log_df.withColumn("timestamp", concat_ws(" ", log_df["date_part"], log_df["time_part"]))

# Convert the timestamp column from string to TimestampType
log_df = log_df.withColumn("timestamp", to_timestamp(log_df["timestamp"], "dd/MM/yy HH:mm:ss"))

# Drop temporary columns
log_df = log_df.drop("date_part", "time_part")

# Show parsed logs
log_df.show(truncate=False)

# Print schema to verify timestamp type
log_df.printSchema()

# Stop Spark Session
spark.stop()
