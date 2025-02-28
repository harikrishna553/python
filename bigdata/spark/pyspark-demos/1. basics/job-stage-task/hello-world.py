from pyspark.sql import SparkSession

# Step 1: Create a Spark session
spark = SparkSession.builder.appName("SparkUIExample").getOrCreate()

# Step 2: Create an in-memory list of data
data = [("Ram", 25), ("Krishna", 30), ("Chamu", 35), ("Sailu", 40)]

# Step 3: Convert the list into a PySpark DataFrame
df = spark.createDataFrame(data, ["Name", "Age"])

# Step 4: Count the total number of elements (rows)
count = df.count()

# Step 5: Print the result
print(f"Total number of rows in DataFrame: {count}")

# Step 6: Pause execution to allow user to check Spark UI
input("Press Enter to exit...")

# Step 7: Stop Spark session
spark.stop()
