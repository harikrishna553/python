from pyspark.sql import SparkSession

# Step 1: Initialize Spark
spark = SparkSession.builder.appName("WordCountRDD").getOrCreate()

# Step 2: Input string
text = "Spark is a powerful engine for big data processing. Spark is fast, Spark is flexible."

# Step 3: Convert the string to an RDD
rdd = spark.sparkContext.parallelize([text])

# Step 4: Split into words, clean, and count
word_counts = (rdd
    .flatMap(lambda line: line.split(" "))  # Split text into words
    .map(lambda word: word.lower().strip(".,!?"))  # Convert to lowercase & clean punctuation
    .filter(lambda word: word != "")  # Remove empty words
    .map(lambda word: (word, 1))  # Create (word, 1) pairs
    .reduceByKey(lambda a, b: a + b)  # Count occurrences
    .sortBy(lambda x: x[1], ascending=False)  # Sort by count descending
)

# Step 5: Collect and print results
for word, count in word_counts.collect():
    print(f"{word}: {count}")

# Stop Spark session
spark.stop()
