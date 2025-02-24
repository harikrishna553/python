from pyspark.sql import SparkSession
from pyspark.sql import Row

def printTitle(title):
    print("*" * 50)
    print(title)
    print("*" * 50)
    return

# Initialize Spark Session
spark = SparkSession.builder.appName("DistinctExample").getOrCreate()

# Sample Data
data = [
    Row(name="Ram", age=25, city="Bangalore"),
    Row(name="Krishna", age=30, city="Chennai"),
    Row(name="Ram", age=25, city="Bangalore"),  # Duplicate row
    Row(name="Sailu", age=22, city="Hyderabad"),
    Row(name="Krishna", age=30, city="Chennai"),  # Duplicate row
]

# Create DataFrame
df = spark.createDataFrame(data)
df.show()

# Get Distinct Rows
printTitle('Distinct Rows')
distinct_df = df.distinct()
distinct_df.show()

# Counting Unique Rows Using distinct().count()
print('Total unique rows:', df.distinct().count())

# Distinct Names
printTitle('Distinct Names')
distinct_names = df.select('name').distinct()
distinct_names.show()