from pyspark import SparkConf, SparkContext

# Boilerplate Spark stuff:
conf = SparkConf().setMaster("local").setAppName("ScorecardsMapReduce")
sc = SparkContext(conf = conf)

#Function to giveout (k,1) from a list given
def func(rdd):
    result = []
    for line in rdd:
        for l in line:
            if( ("Game" not in l) and ("Date" not in l) and ("Goals" not in l)  ):
                kv = l.split("=")
                result.append([kv[0], kv[1]])
    return result			

rawData = sc.textFile("C:\SparkWorkexamples\scorecards1.csv")
rdd = rawData.map(lambda line: line.split(","))
rdd_normalized = func(rdd.collect())
final_rdd = sc.parallelize(rdd_normalized)
mr_result = final_rdd.reduceByKey(lambda a,b: int(a)+int(b))
print("All Process Completed: ")
print(mr_result.collect())