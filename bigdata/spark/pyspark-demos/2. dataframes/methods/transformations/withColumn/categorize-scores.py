from pyspark.sql import SparkSession
from pyspark.sql.functions import expr

# Initialize Spark session
spark = SparkSession.builder.appName("WithColumnExprExample").getOrCreate()

# Sample data
data = [
    (1, "Ram", 90),
    (2, "Krishna", 75),
    (3, "Chamu", 60),
    (4, "Sailu", 45),
    (5, "Hari", 30)
]

# Create DataFrame
columns = ["id", "category", "score"]
df = spark.createDataFrame(data, columns)

# Apply conditional transformation using withColumn and expr with multiple conditions
df_transformed = df.withColumn(
    "grade",
    expr("""
        CASE 
            WHEN score >= 85 THEN 'Distinction'
            WHEN score >= 70 THEN 'First Class'
            WHEN score >= 55 THEN 'Second Class'
            WHEN score >= 40 THEN 'Third Class'
            ELSE 'Failed'
        END
    """)
)

# Show the result
df_transformed.show()
