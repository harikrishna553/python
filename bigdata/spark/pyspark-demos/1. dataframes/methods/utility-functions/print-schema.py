from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("ActionsExample").getOrCreate()

data = [(1, "Ram"), (2, "Krishna"), (3, "Chamu")]

df = spark.createDataFrame(data, ["id", "name"])

df.printSchema()
