from pyspark.sql import SparkSession

# Create a Spark session
spark = SparkSession.builder.appName("EmployeesExample").getOrCreate()

df_direct_csv = (spark
                 .read
                 .option("header", "true")
                 .option("inferSchema", "true")
                 .csv("data/employees.csv"))
df_direct_csv.show()
