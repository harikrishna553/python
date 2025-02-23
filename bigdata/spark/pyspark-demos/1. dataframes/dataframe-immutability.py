from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Step 1: Create a Spark session
spark = SparkSession.builder.appName("ImmutableDF").getOrCreate()

# Step 2: Create a DataFrame
data = [("Ram", 25), ("Krishna", 30), ("Chamu", 35)]
columns = ["Name", "Age"]
df = spark.createDataFrame(data, columns)

# Step 3: Apply transformations (each returns a new DataFrame)
df_filtered = df.filter(col("Age") > 25)  # Filter records where Age > 25
df_selected = df_filtered.select("Name")  # Select only the Name column

# Step 4: Show results
print("Original DataFrame:")
df.show()

print("Filtered DataFrame (Age > 25):")
df_filtered.show()

print("Selected DataFrame (Only Name Column):")
df_selected.show()
