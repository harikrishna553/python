from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.sql.functions import sum

# Initialize Spark Session
spark = SparkSession.builder.appName("RunningTotal").getOrCreate()

# Sample Data
data = [
    (1, 10),
    (2, 20),
    (3, 15),
    (4, 25)
]

# Create DataFrame
df = spark.createDataFrame(data, ["Day", "Expense"])

# Define Window Specification for Running Total
windowSpec = Window.orderBy("Day").rowsBetween(Window.unboundedPreceding, Window.currentRow)

# Apply Running Total Calculation
df = df.withColumn("Running_Total", sum("Expense").over(windowSpec))

# Show Results
df.show()
