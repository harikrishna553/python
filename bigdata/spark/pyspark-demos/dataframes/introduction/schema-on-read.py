from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("SchemaOnRead").getOrCreate()

# Spark will infer the schema automatically
df = spark.read.option("multiLine", "true").json("data/employee.json")  

df.printSchema()
