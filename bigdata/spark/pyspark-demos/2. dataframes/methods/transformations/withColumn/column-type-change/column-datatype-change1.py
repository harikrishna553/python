from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.types import IntegerType, DoubleType

# Initialize Spark session
spark = SparkSession.builder.appName("DataTypeChange").getOrCreate()

# Create a sample DataFrame
data = [("1", "25.5"), ("2", "30.7"), ("3", "45.0")]
df = spark.createDataFrame(data, ["id", "salary"])

# Show original DataFrame
print("Original DataFrame:")
df.show()
df.printSchema()

# Change 'id' to Integer and 'salary' to Double
df_casted = (df.withColumn("id", col("id").cast(IntegerType()))
            .withColumn("salary", col("salary").cast(DoubleType()))
            )

print("DataFrame after type conversion:")
df_casted.show()

# Check Schema
df_casted.printSchema()
