from pyspark.sql import SparkSession, Row
from pyspark.sql.functions import avg, max, min, sum

def printTitle(title):
    print("*" * 50)
    print(title)
    print("*" * 50)
    return

spark = (SparkSession.builder
         .appName("GroupByExamples")
         .getOrCreate())

data = [
    Row(name="Ram", dept="IT", salary=40000),
    Row(name="Krishna", dept="HR", salary=25000),
    Row(name="Chamu", dept="IT", salary=60000),
    Row(name="Sailu", dept="HR", salary=30000),
    Row(name="Gopi", dept="Finance", salary=45000),
]

df = spark.createDataFrame(data)
df.show()

printTitle('Group By Department')
df.groupBy("dept").count().show()

printTitle('Grouping and Summing salaries by department')
df.groupBy("dept").agg(sum("salary").alias("total_salary")).show()

printTitle('Applying Multiple Aggregate Functions')
df.groupBy("dept").agg(
    sum("salary").alias("total_salary"),
    avg("salary").alias("avg_salary"),
    max("salary").alias("max_salary"),
    min("salary").alias("min_salary")
).show()

printTitle('Grouping by Multiple Columns')
df.groupBy("dept", "name").sum("salary").show()

printTitle('Filtering Grouped Data with filter()')
df.groupBy("dept").agg(sum("salary").alias("total_salary")).filter("total_salary > 80000").show()