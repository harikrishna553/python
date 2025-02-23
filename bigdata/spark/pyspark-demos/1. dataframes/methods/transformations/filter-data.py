from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("ActionsExample").getOrCreate()

data = [(1, "Ram"), (2, "Krishna"), (3, "Chamu")]

df = spark.createDataFrame(data, ["id", "name"])

even_id_df = df.filter(df.id % 2 == 0)

# Action: Triggers execution
even_id_df.show()
