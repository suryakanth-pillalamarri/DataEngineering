from pyspark.sql import SparkSession

spark=SparkSession.builder.appName('Test').getOrCreate()

print('Installed Spark varsion:',spark.version)
spark.stop()