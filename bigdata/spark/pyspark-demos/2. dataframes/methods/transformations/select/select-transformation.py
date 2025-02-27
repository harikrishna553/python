from pyspark.sql import SparkSession
from pyspark.sql.functions import col, upper, expr

def printTitle(title):
    print("*" * 50)
    print(title)
    print("*" * 50)
    return

# Create Spark session
spark = (SparkSession.builder
         .appName("SelectTransformation")
         .getOrCreate())

# Sample Data
data = [("Ram", 25, "Bangalore"), 
        ("Krishna", 30, "Hyderabad"), 
        ("Chamu", 35, "Chennai")]

columns = ["name", "age", "city"]

df = spark.createDataFrame(data, columns)
df.show()

# Select name and age columns
printTitle('Selecting name and age columns')
df.select("name", "age").show()
df.select(col("name"), col("city")).show()

# Renaming Columns Using alias
printTitle('Renaming Columns Using alias')
df.select(col("name").alias("full_name"), col("age")).show()

# Apply transformations using built in functions
printTitle('Apply transformations using built in functions')
df.select(col("name"), upper(col("city")).alias("CITY_UPPERCASE")).show()

# Using Expressions in select
printTitle('Using Expressions in select')
df.select(col("name"), (col("age") + 5).alias("age_plus_5")).show()

# Using SQL Expressions
printTitle('Using SQL Expressions')
df.selectExpr("name", "age * 2 as double_age").show()

# Selecting Columns Dynamically based on a list
printTitle('Selecting Columns Dynamically based on a list')
columns_to_select = ["name", "age"]
df.select(*columns_to_select).show()

# Selecting All Columns
printTitle("Selecting All Columns")
df.select("*").show()

# Selecting All Columns with Additional Expressions
printTitle("Selecting All Columns with Additional Expressions")
df.select("*", (col("age") * 2).alias("double_age")).show()
