#Import Libraries
from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession
from pyspark.sql.functions import *

#Parameters to listen socket 
host = "127.0.0.1"
port = "9999"

#Create Spark Session
spark = SparkSession \
        .builder \
        .appName("firstSparkStreaming") \
        .getOrCreate()

#Create Streaming DataFrame by socket input source
initDF = (spark
  .readStream
  .format("socket")
  .option("host", host)
  .option("port", port)
  .load())

# UDF for case insensitive
caseinsensitiveUDF = udf(lambda x: x.upper())

#Dataframe printSchema
wordCount = (initDF
  .select(explode(split(caseinsensitiveUDF(col("value")), " ")).alias("words"))
  .groupBy("words")
  .count()
  )
wordCount.printSchema()

#Show streaming DataFrame
wordCount.writeStream \
  .outputMode("complete") \
  .option("truncate", False) \
  .format("console") \
  .start() \
  .awaitTermination()