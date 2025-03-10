from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

# Create a Spark session
spark = SparkSession.builder.appName("RDDtoDataFrame").getOrCreate()

# Sample data
data = [
    (1, "Ram", 29),
    (2, "Krishna", 35),
    (3, "chamu", 40)
]

# Create an RDD from the data
my_rdd = spark.sparkContext.parallelize(data)

# Define the schema
my_schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("name", StringType(), True),
    StructField("age", IntegerType(), True)
])

# Convert RDD to DataFrame
my_df = spark.createDataFrame(my_rdd, schema=my_schema)

# Show the DataFrame
my_df.show()
