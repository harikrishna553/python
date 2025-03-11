from pyspark.sql import SparkSession
from pyspark.sql import Row

# Create Spark Session
spark = (SparkSession.builder
         .appName("RenameColumnsExample")
         .getOrCreate())

# Create Data
dataList = [
    (1, "Ram", 25),
    (2, "Krishna", 30),
    (3, "Chamu", 35)
]

# Convert Data to DataFrame (without custom column names)
print('DataFrame')
df = spark.createDataFrame(dataList)
df.show()

# Add columns to the df
print('\nDataFrame With Column Names')
dfWithColumnNames = df.toDF('Id', 'Name', 'Age')
dfWithColumnNames.show()