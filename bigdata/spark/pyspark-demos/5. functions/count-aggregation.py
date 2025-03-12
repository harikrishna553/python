from pyspark.sql import SparkSession
from pyspark.sql.functions import count

# Initialize Spark Session
spark = SparkSession.builder.appName("CountExample").getOrCreate()

# Sample Data
data = [
    (1, "Ram", 3000),
    (2, "Krishna", 4000),
    (3, "Chamu", None),  # Null Salary
    (4, "Sailu", 4500),
    (None, None, None),       # Null Record
    (6, "Gopi", 6500),
]

columns = ["ID", "Name", "Salary"]

df = spark.createDataFrame(data, columns)
df.show()

df.selectExpr("count(1) as Count_1").show()
df.selectExpr("count(*) as Count_Star").show()
df.select(count("Salary").alias("Count_Salary")).show()


