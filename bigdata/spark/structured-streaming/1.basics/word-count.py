from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split

# Create Spark Session
spark = SparkSession.builder \
    .appName("WordCountStreaming") \
    .getOrCreate()

# Define the input directory
input_dir = "/Users/Shared/streaming_input"

# Read text files as a streaming source
lines = spark.readStream \
    .format("text") \
    .load(input_dir)

# Split lines into words
words = lines.select(explode(split(lines.value, " ")).alias("word"))

# Count occurrences of each word
word_counts = words.groupBy("word").count()

# Write the word count result to the console
query = word_counts.writeStream \
    .outputMode("complete") \
    .format("console") \
    .start()

# Keep the streaming query running
query.awaitTermination()
