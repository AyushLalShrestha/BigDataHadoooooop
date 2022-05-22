## Links
https://cloud.ibm.com/docs/services/Cloudant?topic=cloudant-cap-theorem
https://realpython.com/blog/python/introduction-to-mongodb-and-python/
https://docs.mongodb.com/manual/tutorial/query-documents/#read-operations-query-argument
https://docs.mongodb.com/manual/crud/
https://docs.mongodb.com/v3.0/reference/sql-comparison/
https://www.tutorialspoint.com/mongodb/mongodb_regular_expression.htm
https://hackernoon.com/mongodb-transactions-5654cdb8fd24
https://stackoverflow.com/questions/51238986/pymongo-transaction-errortransaction-numbers-are-only-allowed-on-a-replica-set
https://docs.mongodb.com/manual/sharding/
https://dba.stackexchange.com/questions/52632/difference-between-sharding-and-replication-on-mongodb#:~:text=A%20Replica%2DSet%20means%20that,the%20data%20of%20each%20other.&text=A%20Sharded%20Cluster%20means%20that,cluster%20where%20the%20data%20resides.
https://www.mongodb.com/blog/post/processing-2-billion-documents-a-day-and-30tb-a
https://www.mongodb.com/blog/post/performance-best-practices-transactions-and-read--write-concerns
https://www.linode.com/docs/guides/creating-a-mongodb-replication-set-on-ubuntu-16-04/
https://www.linode.com/docs/guides/build-database-clusters-with-mongodb/
https://kchodorow.com/2010/03/30/sharding-with-the-fishes/
https://docs.mongodb.com/manual/tutorial/deploy-shard-cluster/
https://stackoverflow.com/questions/6635718/how-to-work-around-the-lack-of-transactions-in-mongodb

mongod --dbpath /tmp/mongodata  --replSet rs0 --journal --bind_ip 127.0.0.1 --quiet
mongod --dbpath /tmp/mongodata --journal --bind_ip 127.0.0.1 --quiet

use makalu
db.persons.insert({"name": "Ayush", "age": 23})
db.createUser({	
    user: "makalu",
	pwd: "makalu-wzkzlu-LI5",
    roles:[{role: "userAdminAnyDatabase" , db:"makalu"}]
})



mongod --port 27017 --dbpath ~/data/makalu
use admin
db.createUser({
    user: "makalu",
	pwd: "makalu-wzkzlu-LI5",
    roles:[{role: "userAdminAnyDatabase" , db:"admin"}]
})
mongod --auth --port 27017 --dbpath ~/data/makalu
mongo admin  -u makalu -p makalu-wzkzlu-LI5

mongod --port 27017 --dbpath ~/data/makalu --replSet rs0 --bind_ip localhost


# Mongo geospatial data
# Aggregation pipeline
# 

