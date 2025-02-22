from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

spark = SparkSession.builder.appName("SchemaOnRead").getOrCreate()

schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("name", StringType(), True),
    StructField("age", IntegerType(), True)
])

# Spark will infer the schema automatically
df = spark.read.option("multiLine", "true").schema(schema).json("data/employee.json")  

df.printSchema()
