from pyspark.sql import SparkSession

# Initialize Spark Session
spark = SparkSession.builder.appName("ReadSparkFileFormats").getOrCreate()

def print_section(title):
    print("\n" + "=" * 50)
    print(f"{title}")
    print("=" * 50 + "\n")

# Read JSON
df_json = spark.read.json("data/employees_json")
print_section("Reading JSON Data")
df_json.show()

# Read CSV
df_csv = spark.read.option("header", "true").csv("data/employees_csv")
print_section("Reading CSV Data")
df_csv.show()

# Read Parquet
df_parquet = spark.read.parquet("data/employees_parquet")
print_section("Reading Parquet Data")
df_parquet.show()

# Read ORC
df_orc = spark.read.orc("data/employees_orc")
print_section("Reading ORC Data")
df_orc.show()

# Read Text (Extract JSON strings from text file)
df_text = spark.read.text("data/employees_text")
print_section("Reading Text Data")
df_text.show(truncate=False)

# Stop Spark Session
spark.stop()
