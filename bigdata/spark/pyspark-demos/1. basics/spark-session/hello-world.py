from pyspark.sql import SparkSession

# Create a Spark Session
spark = (SparkSession.builder 
    .appName("DataProcessingApp")   # Name of the application
    .master("local[*]")   # Run Spark locally using all available cores
    .getOrCreate())  # Creates a session if not exists, otherwise returns existing one

# Create Sample Data
data = [("Ram", 30, "HR"),
        ("Krishna", 25, "IT"),
        ("Chamu", 28, "Finance")]

columns = ["Name", "Age", "Department"]

# Create DataFrame
df = spark.createDataFrame(data, columns)

# Show Data
df.show()

# Stop the session
spark.stop()
