from pyspark.sql import SparkSession

# Step 1: Initialize Spark
spark = SparkSession.builder.appName("EmployeeDataRDD").getOrCreate()

# Step 2: Read CSV file as an RDD
rdd = spark.sparkContext.textFile("employees.csv")

# Step 3: Extract header and process data
header = rdd.first()  # Extract header row
employee_rdd = rdd.filter(lambda line: line != header)  # Remove header

# Step 4: Parse CSV and extract (department, salary)
department_salaries = (employee_rdd
    .map(lambda line: line.split(","))  # Split CSV line into fields
    .map(lambda fields: (fields[2], int(fields[3])))  # Extract (department, salary)
    .reduceByKey(lambda a, b: a + b)  # Sum salaries by department
    .sortBy(lambda x: x[1], ascending=False)  # Sort by total salary descending
)

# Step 5: Collect and print results
for department, total_salary in department_salaries.collect():
    print(f"{department}: ${total_salary}")

# Stop Spark session
spark.stop()
