from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.sql.functions import avg, to_date

# Initialize Spark Session
spark = SparkSession.builder.appName("MovingAverage").getOrCreate()

# Sample Data (Date as String)
data = [
    ("2024-01-01", 100),
    ("2024-01-02", 102),
    ("2024-01-03", 105),
    ("2024-01-04", 110),
    ("2024-01-05", 120),
    ("2024-01-06", 120),
    ("2024-01-07", 130),
    ("2024-01-08", 128)
]

# Create DataFrame
df = spark.createDataFrame(data, ["Date", "Stock_Price"])

# Convert "Date" column from string to DateType
df = df.withColumn("Date", to_date(df["Date"], "yyyy-MM-dd"))

# Define Window Specification for 7-Day Moving Average
windowSpec = Window.orderBy("Date").rowsBetween(-6, Window.currentRow)

# Apply Moving Average Calculation
df = df.withColumn("7_day_Moving_Avg", avg("Stock_Price").over(windowSpec))

# Show Results
df.show()
