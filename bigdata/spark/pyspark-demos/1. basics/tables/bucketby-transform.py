from pyspark.sql import SparkSession
from pyspark.sql import Row

# Step 1: Set up SparkSession
spark = (SparkSession.builder 
    .appName("PySpark BucketBy Example") 
    .master("local[*]")
    .config("spark.sql.warehouse.dir", "/tmp/spark-warehouse")
    .getOrCreate())

# Step 2: Create a Sample DataFrame
# Sample transaction data with Indian names, states, and cities
data = [
    Row(1, "Amit", "Maharashtra", "Mumbai", 5000),
    Row(2, "Priya", "Karnataka", "Bangalore", 7000),
    Row(3, "Rajesh", "Delhi", "New Delhi", 4000),
    Row(4, "Sita", "Tamil Nadu", "Chennai", 9000),
    Row(5, "Rahul", "West Bengal", "Kolkata", 6000),
    Row(6, "Neha", "Gujarat", "Ahmedabad", 4500),
    Row(7, "Vikram", "Punjab", "Amritsar", 8000),
    Row(8, "Kavita", "Rajasthan", "Jaipur", 5500),
    Row(9, "Manoj", "Uttar Pradesh", "Lucknow", 7200),
    Row(10, "Pooja", "Bihar", "Patna", 3800),
    Row(11, "Arun", "Madhya Pradesh", "Bhopal", 6200),
    Row(12, "Sunita", "Odisha", "Bhubaneswar", 4700),
    Row(13, "Ravi", "Andhra Pradesh", "Vijayawada", 5300),
    Row(14, "Meera", "Telangana", "Hyderabad", 8100),
    Row(15, "Gaurav", "Haryana", "Gurgaon", 7700),
    Row(16, "Anjali", "Himachal Pradesh", "Shimla", 4900),
    Row(17, "Vivek", "Assam", "Guwahati", 4200),
    Row(18, "Sanjay", "Goa", "Panaji", 5800),
    Row(19, "Deepika", "Jharkhand", "Ranchi", 6700),
    Row(20, "Kiran", "Chhattisgarh", "Raipur", 6100)
]

columns = ["customer_id", "name", "state", "city", "amount"]
df = spark.createDataFrame(data, columns)

df.show()

# Step 3: Writing Data Using bucketBy
(df.write
    .format("csv") \
    .bucketBy(3, "state", "city") 
    .sortBy("state", "city")
    .mode("overwrite")
    .saveAsTable("bucketed_transactions"))

# Step 4: Reading the Bucketed Data
bucketed_df = spark.read.table("bucketed_transactions")
bucketed_df.show()