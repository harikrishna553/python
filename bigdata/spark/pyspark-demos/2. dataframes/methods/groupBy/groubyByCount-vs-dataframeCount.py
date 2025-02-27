from pyspark.sql import SparkSession

def printTitle(title):
    print("\n")
    print("*" * 50)
    print(title)
    print("*" * 50)
    return

# Initialize Spark Session
spark = SparkSession.builder.appName("CountExamples").getOrCreate()

# Sample Data
data = [
    ("Ram", "IT", 5000),
    ("Krishna", "HR", 4000),
    ("Chamu", "IT", 6000),
    ("Sailu", "HR", 4500),
    ("Gopi", "Finance", 7000),
]

# Create DataFrame
df = spark.createDataFrame(data, ["name", "dept", "salary"])
df.show()

# Count total number of rows in DataFrame
total_count = df.count()
print(f"Total number of rows in DataFrame: {total_count}")

# Count records by group
printTitle('Count records by group')
df.groupBy("dept").count().show()

printTitle('Counting the Number of Groups After groupBy')
print(f'Total Unique Departments : {df.groupBy("dept").count().count()}')
print(f'Total Unique Departments : {df.select("dept").distinct().count()}')