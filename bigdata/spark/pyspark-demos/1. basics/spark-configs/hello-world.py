from pyspark.sql import SparkSession
from pyspark import SparkConf

# Configure Spark
conf = SparkConf() \
    .set("spark.app.name", "MyApp") \
    .set("spark.executor.memory", "4g")

spark = SparkSession.builder.config(conf=conf).getOrCreate()

print(f"Application Name: {spark.conf.get('spark.app.name')}")
print(f"Executor Memory: {spark.conf.get('spark.executor.memory')}")

spark.stop()