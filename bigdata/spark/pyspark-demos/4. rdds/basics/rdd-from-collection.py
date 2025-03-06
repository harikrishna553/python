from pyspark.sql import SparkSession

# Step 1: Initialize Spark Session
spark = SparkSession.builder.appName("EnhancedRDDExample").getOrCreate()
sc = spark.sparkContext  # SparkContext

# Step 2: Create an RDD from a list
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
rdd = sc.parallelize(data)

# Step 3: Apply transformations
squared_rdd = rdd.map(lambda x: x ** 2)  # Square each number
filtered_rdd = squared_rdd.filter(lambda x: x % 2 == 0)  # Keep only even squares

# Step 4: Perform an action
sum_of_even_squares = filtered_rdd.reduce(lambda a, b: a + b)  # Sum even squares

# Step 5: Collect and print results
print("Original RDD:", rdd.collect())  
print("Squared RDD:", squared_rdd.collect())  
print("Filtered Even Squares:", filtered_rdd.collect())  
print("Sum of Even Squares:", sum_of_even_squares)  

# Step 6: Stop Spark session
spark.stop()
