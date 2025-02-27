from pyspark.sql import SparkSession

spark1 = SparkSession.builder.appName("Spark1").getOrCreate()
print(f"spark1 : {spark1}")
spark1.stop() # Stops the SparkSession and SparkContext

spark2 = SparkSession.builder.appName("Spark2").getOrCreate()
print(f"spark2 : {spark2}")
print(f"spark1 is spark2: {spark1 is spark2}") # will return false
print(f"spark1.sparkContext is spark2.sparkContext: {spark1.sparkContext is spark2.sparkContext}") # Will throw error, because spark1.sparkContext is stopped.

spark2.stop()