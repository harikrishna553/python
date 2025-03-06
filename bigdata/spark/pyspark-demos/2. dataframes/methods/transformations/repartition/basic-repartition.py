from pyspark.sql import SparkSession

# Initialize Spark Session
spark = SparkSession.builder.appName("HashPartitioningExample").getOrCreate()

# Sample DataFrame
df = spark.createDataFrame([
    (1, "Ram", 25),
    (2, "Hari", 30),
    (3, "Krishna", 35),
    (4, "Chamu", 40),
    (5, "Sailu", 45),
    (6, "Gopi", 50),
    (7, "Joel", 55),
    (8, "Vandana", 60)
], ["id", "name", "age"])

# Show original DataFrame
print("Original DataFrame:")
df.show()

# Check the default number of partitions
print(f"Default partitions: {df.rdd.getNumPartitions()}")

# Perform Hash Partitioning on 'id' column into 4 partitions
num_partitions = 4
df_partitioned = df.repartition(num_partitions)

# Show partition details
print(f"After partitioning (Partitions: {df_partitioned.rdd.getNumPartitions()}):")

# Display partition-wise data
partition_data = df_partitioned.rdd.mapPartitionsWithIndex(
    lambda index, rows: [(index, list(rows))]).collect()

for partition, data in partition_data:
    print(f"Partition {partition}: {data}")

# Stop Spark Session
spark.stop()
