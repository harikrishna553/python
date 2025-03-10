from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

# Create Spark session
spark = SparkSession.builder.appName("UDF Example").getOrCreate()

# Define the function
def capitalize_first_letter(name):
    return name.capitalize() if name else None

# Register UDF
capitalize_udf = udf(capitalize_first_letter, StringType())

# Fix: Ensure tuples in the list
data = [("ram",), ("krishna",), ("sailu",)]  

# Create DataFrame
df = spark.createDataFrame(data, ["name"])

# Apply UDF
df = df.withColumn("capitalized_name", capitalize_udf(df["name"]))

# Show results
df.show()
