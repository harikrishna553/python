from pyspark.sql import SparkSession

# Initialize Spark Session
spark = SparkSession.builder.appName("HashPartitioningExample").getOrCreate()

# Sample DataFrame
df = spark.createDataFrame([
    (1, "Ram", 25, "Bangalore"),
    (2, "Hari", 30, "Chennai"),
    (3, "Krishna", 35, "Hyderabad"),
    (4, "Chamu", 40, "Mumbai"),
    (5, "Sailu", 45, "Bangalore"),
    (6, "Gopi", 50, "Mumbai"),
    (7, "Joel", 55, "Mumbai"),
    (8, "Vandana", 60, "Amaravathi"),
    (9, "Ramesh", 50, "Delhi"),
    (10, "Suresh", 45, "Delhi")
], ["id", "name", "age", "city"])

# Show original DataFrame
print("Original DataFrame:")
df.show()

# Check the default number of partitions
print(f"Default partitions: {df.rdd.getNumPartitions()}")

# Perform Hash Partitioning on 'id' column into 4 partitions
num_partitions = 4
df_partitioned = df.repartition(num_partitions, "city")

# Show partition details
print(f"After hash partitioning on 'city' (Partitions: {df_partitioned.rdd.getNumPartitions()}):")

df_partitioned.write.mode("overwrite").csv("/Users/Shared/new-data")

# Stop Spark Session
spark.stop()
