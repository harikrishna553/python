from pyspark.sql import SparkSession

# Initialize Spark Session
spark = SparkSession.builder.appName("EmployeeRDD").getOrCreate()

# List of employee records (ID, Name, Age, Department, Salary)
employees = [
    (1, "Ram", 30, "HR", 50000),
    (2, "Krishna", 25, "IT", 70000),
    (3, "Chamu", 35, "Finance", 90000),
    (4, "Sailu", 40, "IT", 85000),
    (5, "Gopi", 28, "HR", 48000)
]

# Convert the list to an RDD
employee_rdd = spark.sparkContext.parallelize(employees)

# Collect and print the RDD
print("Original Employee RDD:")
print(employee_rdd.collect())

# Filter employees belonging to IT department
it_employees = employee_rdd.filter(lambda emp: emp[3] == "IT")

print("\nIT Employees:")
print(it_employees.collect())

# Extract salaries
salaries = employee_rdd.map(lambda emp: emp[4])

# Compute average salary
total_salary = salaries.reduce(lambda x, y: x + y)
average_salary = total_salary / employee_rdd.count()

print(f"\nAverage Salary: {average_salary}")

# Sort employees by age (ascending order)
sorted_by_age = employee_rdd.sortBy(lambda emp: emp[2])

print("\nEmployees Sorted by Age:")
print(sorted_by_age.collect())


