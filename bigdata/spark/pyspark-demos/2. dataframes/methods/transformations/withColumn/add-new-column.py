from pyspark.sql import SparkSession
from pyspark.sql.functions import lit

# Create a Spark session
spark = (SparkSession.builder
         .appName("WithColumnExample")
         .getOrCreate())

# Sample DataFrame
data = [("Ram", 25), ("Krishna", 30), ("Chamu", 35)]
df = spark.createDataFrame(data, ["Name", "Age"])

# Adding a new column 'Country' with a default value
df_new = df.withColumn("Country", lit("India"))

# Show the results
df_new.show()
