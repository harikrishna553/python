from pyspark.sql import SparkSession

# Step 1: Initialize Spark Session
spark = (SparkSession.builder
    .appName("PySpark MySQL Example")
    .config("spark.jars", "/Users/krishna/Downloads/mysql-connector-j-9.2.0.jar")  # Update path
    .getOrCreate())

# Step 2: MySQL Database Connection Details
jdbc_url = "jdbc:mysql://localhost:3306/pysparkdemo"  # Update if needed
table_name = "Employee"
user = "root"  # Change if needed
connection_properties = {
    "user": user,
    "password": "tiger",  # Change if needed
    "driver": "com.mysql.cj.jdbc.Driver"
}

# Step 3: Load MySQL Table into PySpark DataFrame
df = (spark
      .read
      .jdbc(url=jdbc_url, table=table_name, properties=connection_properties))

# Display DataFrame
print("Original Employee Table:")
df.show()

# Step 4: Cache the Table in Memory
df.cache()
df.count()  # Action to trigger caching
print("Table Cached Successfully!")

# Step 5: Register DataFrame as a Temporary SQL Table
df.createOrReplaceTempView("EmployeeTable")

# Run SQL Query on Cached Table
print("Query Result for Employees in IT Department:")
result = spark.sql("SELECT * FROM EmployeeTable WHERE Department = 'IT'")
result.show()

# Step 6: Unpersist Cache (Optional)
df.unpersist()

# Stop Spark Session
spark.stop()