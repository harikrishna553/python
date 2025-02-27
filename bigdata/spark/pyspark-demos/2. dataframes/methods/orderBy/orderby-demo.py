from pyspark.sql import SparkSession
from pyspark.sql.functions import col

def printTitle(title):
    print("*" * 50)
    print(title)
    print("*" * 50)
    return

# Initialize Spark Session
spark = (SparkSession.builder
         .appName("OrderByExample")
         .getOrCreate())

# Sample Data
data = [
    (1, "Ram", 30),
    (2, "Krishna", 25),
    (3, "Chamu", 35),
    (4, "Sailu", 28),
    (5, "Thulasi", 30)
]

# Creating DataFrame
columns = ["id", "name", "age"]
df = spark.createDataFrame(data, columns)
df.show()

printTitle('Order By Age In Ascending Order')
df.orderBy("age").show()
df.orderBy(col("age").asc()).show()

printTitle('Order By Age In Descending Order')
df.orderBy(col("age").desc()).show()

print('Sorting by multiple columns (ascending & descending mix)')
df.orderBy(col("age").asc(), col("name").desc()).show()
