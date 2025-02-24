from pyspark.sql import SparkSession
from pyspark.sql.functions import col

def printTitle(title):
    print("*" * 50)
    print(title)
    print("*" * 50)
    return

# Create a Spark session
spark = (SparkSession.builder
         .appName("WhereTransformation")
         .getOrCreate())

data = [
    (1, "Ram", 25, "Engineer"),
    (2, "Krishna", 30, "Doctor"),
    (3, "Chamu", 35, "Artist"),
    (4, "Sailu", 40, "Engineer"),
    (5, "Gopi", 28, "Doctor")
]

columns = ["id", "name", "age", "profession"]
df = spark.createDataFrame(data, columns)
df.show()

# Select all rows where age is greater than 30.
printTitle('Select all rows where age is greater than 30.')
df.where(df.age > 30).show()
df.where(col("age") > 30).show()
# Using SQL Like Syntax
df.where("age > 30").show()

# Select all rows where profession is "Engineer".
printTitle('Select all rows where profession is "Engineer".')
df.where(df.profession == "Engineer").show()
df.where(col("profession") == "Engineer").show()
df.where("profession == 'Engineer'").show()

# Select all rows where age is greater than 25 AND profession is "Doctor".
printTitle('Select all rows where age is greater than 25 AND profession is "Doctor"')
df.where((df.age > 25) & (df.profession == "Doctor")).show()
df.where((col("age") > 25) & (col("profession") == 'Doctor')).show()
df.where("age > 25 AND profession = 'Doctor'").show()

# Select all rows where age is less than 30 OR profession is "Engineer".
printTitle('Select all rows where age is less than 30 OR profession is "Engineer".')
df.where((df.age < 30) | (df.profession == "Engineer")).show()
df.where((col('age') < 30) | (col('profession') == "Engineer")).show()
df.where("age < 30 OR profession = 'Engineer'").show()

# Select all rows where profession is NOT "Engineer".
printTitle('Select all rows where profession is NOT "Engineer".')
df.where(df.profession != "Engineer").show()
df.where(col('profession') != "Engineer").show()
df.where("profession != 'Engineer'").show()

# Select all rows where the name starts with "K".
printTitle('Select all rows where the name starts with "K".')
df.where(df.name.like("K%")).show()
df.where(col('name').like("K%")).show()
df.where("name LIKE 'K%'").show()

# Select all rows where profession is either "Engineer" or "Doctor".
printTitle('Select all rows where profession is either "Engineer" or "Doctor".')
df.where(df.profession.isin(["Engineer", "Doctor"])).show()
df.where(col("profession").isin(["Engineer", "Doctor"])).show()
df.where("profession IN ('Engineer', 'Doctor')").show()

# Select all rows where age is between 25 and 35.
printTitle('Select all rows where age is between 25 and 35.')
df.where(df.age.between(25, 35)).show()
df.where(col("age").between(25, 35)).show()
df.where("age BETWEEN 25 AND 35").show()