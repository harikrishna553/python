from pyspark.sql import SparkSession

# Create a Spark session
spark = (SparkSession.builder.appName("EmployeesExample")
.master('local[3]')
.getOrCreate())

# Sample employee data (ID, Name, Age, Department, Salary)
data = [
    (1, "Krishna", 30, "HR", 55000),
    (2, "Chamu", 27, "IT", 62000),
    (3, "Sailaja", 35, "Finance", 75000),
    (4, "Rama Krishna", 40, "IT", 85000),
    (5, "Joel", 26, "HR", 47000)
]

# Define column names
columns = ["ID", "Name", "Age", "Department", "Salary"]

# Create a DataFrame
df = spark.createDataFrame(data, columns)

# Show the DataFrame
print("### Employee Data ###")
df.show()

# Filter employees in IT department
print("### Employees in IT Department ###")
df.filter(df.Department == "IT").show()

# Show employees with Salary greater than 50,000
print("### Employees with Salary > 50,000 ###")
df.filter(df.Salary > 50000).show()

# Group by Department and show average salary
print("### Average Salary by Department ###")
df.groupBy("Department").avg("Salary").show()

# Stop the Spark session
spark.stop()
