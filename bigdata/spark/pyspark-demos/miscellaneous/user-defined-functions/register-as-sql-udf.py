from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

# Create Spark session
spark = SparkSession.builder.appName("UDF Example").getOrCreate()

# Define the function
def capitalize_first_letter(name):
    return name.capitalize() if name else None

# Register UDF
spark.udf.register("capitalize_sql", capitalize_first_letter, StringType())

# Fix: Ensure tuples in the list
data = [("ram",), ("krishna",), ("sailu",)]  

# Create DataFrame
df = spark.createDataFrame(data, ["name"])

df.createOrReplaceTempView("people")

# Apply UDF
result = spark.sql("SELECT name, capitalize_sql(name) AS capitalized_name FROM people")

# Show results
result.show()
