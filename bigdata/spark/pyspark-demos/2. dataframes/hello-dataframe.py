from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("SparkExample").getOrCreate()

# Sample Employee Data
columns = ["ID", "Name", "Age", "Department", "Salary"]
data = [
    (1, "Ram", 30, "HR", 50000),
    (2, "Krishna", 25, "IT", 60000),
    (3, "Chamu", 35, "Finance", 70000),
    (4, "Sailu", 40, "IT", 80000)
]

df = spark.createDataFrame(data, schema=columns)

# Filter employees in IT department
it_df = df.filter(df.Department == "IT")

# Select only the 'Name' column
it_df.select("Name").show()
