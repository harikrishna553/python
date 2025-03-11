from pyspark.sql import SparkSession
from pyspark.sql.functions import monotonically_increasing_id

# Initialize Spark session
spark = SparkSession.builder.appName("MonotonicIDExample").getOrCreate()

# Sample data
data = [("Ram", 23), ("Krishna", 30), ("Chamu", 29), ("Sailu", 35), ("Gopi", 40)]
columns = ["Name", "Age"]

# Create DataFrame
df = spark.createDataFrame(data, columns)

# Repartition the DataFrame to simulate distributed processing
df = df.repartition(3)

# Add a unique, monotonically increasing ID column
df = df.withColumn("id", monotonically_increasing_id())

# Show results
df.show()
