from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, count, max, min, sum

# Create a Spark session
spark = SparkSession.builder.appName("AggregationExample").getOrCreate()

data = [
    ("Ram", "Sales", 3000),
    ("Krishna", "Sales", 4000),
    ("Chamu", "HR", 5000),
    ("Sailu", "HR", 4500),
    ("Gopi", "IT", 6000),
    ("Jaideep", "IT", 6500),
]

columns = ["Employee", "Department", "Salary"]

df = spark.createDataFrame(data, columns)
df.show()

df_insights = df.select(avg("Salary").alias("Average_Salary"),
                        count("Salary").alias("Total_Employees"),
                        max("Salary").alias("Max_Salary"),
                        min("Salary").alias("Min_Salary"),
                        sum("Salary").alias("Total_Salary"),
                        )

df_insights.show()

# Aggregating with GroupBy
df.groupBy("Department").agg(
    avg("Salary").alias("Avg_Salary"),
    sum("Salary").alias("Total_Salary"),
    max("Salary").alias("Max_Salary")
).show()

df.selectExpr('avg(Salary) as `Average Salary`',
              'max(Salary) as MaxSalary').show()