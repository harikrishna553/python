from pyspark.sql import SparkSession

# Initialize Spark session with a custom warehouse location
spark = (SparkSession.builder
    .appName("SaveAsTableExample")
    .config("spark.sql.warehouse.dir", "/tmp/spark-warehouse")  # Set metastore location
    .getOrCreate())

# Create a sample DataFrame
data = [(1, "Ram", 30), (2, "Krishna", 25), (3, "Chamu", 35)]
columns = ["id", "name", "age"]

df = spark.createDataFrame(data, columns)

# Save DataFrame as a Hive table in Parquet format
df.write.mode("overwrite").format("csv").saveAsTable("user_table")

# Read the table using SQL
df2 = spark.sql("SELECT * FROM user_table")
df2.show()
