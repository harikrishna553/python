from pyspark.sql import SparkSession

# Initialize Spark
spark = SparkSession.builder.appName("SparkExample").getOrCreate()
sc = spark.sparkContext  # Get SparkContext

# Sample Employee Data
data = [
    (1, "Ram", 30, "HR", 50000),
    (2, "Krishna", 25, "IT", 60000),
    (3, "Chamu", 35, "Finance", 70000),
    (4, "Sailu", 40, "IT", 80000)
]

# Create an RDD
rdd = sc.parallelize(data)

# Filter employees in IT department
it_employees = rdd.filter(lambda emp: emp[3] == "IT")

# Get the names of IT employees
it_employee_names = it_employees.map(lambda emp: emp[1]).collect()

print("IT Employee Names using RDD:", it_employee_names)
