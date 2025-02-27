from pyspark import SparkConf, SparkContext

conf = SparkConf() \
    .setAppName("MyApp") \
    .setMaster("local[2]") \
    .set("spark.executor.memory", "2g") \
    .set("spark.driver.memory", "1g")

sc = SparkContext(conf=conf)
print(sc.getConf().getAll()) 
