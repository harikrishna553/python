from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("ConfigExample").getOrCreate()
conf = spark.sparkContext.getConf()

# Get specific config value
app_name = conf.get("spark.app.name")
print(f"Application Name: {app_name}")

conf.set('spark.app.name', 'Chat Server')
app_name = conf.get("spark.app.name")
print(f"Application Name: {app_name}")