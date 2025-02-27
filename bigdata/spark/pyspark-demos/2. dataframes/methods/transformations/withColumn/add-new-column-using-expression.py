from pyspark.sql import SparkSession
from pyspark.sql.functions import expr

# Create a Spark session
spark = (SparkSession.builder
         .appName("WithColumnExample")
         .getOrCreate())

# Sample DataFrame
data = [("Ram", 25), ("Krishna", 30), ("Chamu", 35)]
df = spark.createDataFrame(data, ["Name", "Age"])

# Create a column based on a condition
df_expr = df.withColumn("Age_Group", expr("CASE WHEN Age < 30 THEN 'Young' ELSE 'Adult' END"))

# Show the results
df.show()
df_expr.show()
