from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("ConfigExample").getOrCreate()
conf = spark.sparkContext.getConf()

# Get specific config value
app_name = conf.get("spark.app.name")
print(f"Application Name: {app_name}")

# List all configurations
for k, v in conf.getAll():
    print(f"{k} = {v}")
