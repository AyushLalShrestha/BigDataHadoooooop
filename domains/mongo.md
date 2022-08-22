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

use annapurna
db.persons.insert({"name": "Ayush", "age": 23})
db.createUser({	
    user: "annapurna",
	pwd: "annapurna-np1",
    roles:[{role: "userAdminAnyDatabase" , db:"annapurna"}]
})


# Initializing Mongo 
mongod --port 27017 --dbpath ~/data/annapurna
use admin
db.createUser({
    user: "annapurna",
	pwd: "annapurna-np1",
    roles:[{role: "userAdminAnyDatabase" , db:"admin"}]
})
mongod --auth --port 27017 --dbpath ~/data/annapurna
mongo admin  -u annapurna -p annapurna-np1

mongod --port 27017 --dbpath ~/data/annapurna --replSet rs0 --bind_ip localhost

Topics to learn:
    # Mongo geospatial data
    # Aggregation pipeline

Aggregation link: mongo tutorialspoint aggregation




# Mongo DB Cheat Sheet:
#Miscallenous:
db.collection.find(<query>)	
coll.find().sort( { name: 1 } );
db.collection.find( ... ).limit( 5 )	 
db.collection.find( ... ).skip( <n> 
db.collection.find(<query>).count()
db.collection.findOne(<query>)	 

Search and Find Queries:

#aggregation:
 select by_user, count(*) from mycol group by by_user
db.mycol.aggregate([{$group : {_id : "$user", num_tutorial : {$sum : 1}}}])
{ 
db.mycol.aggregate([{$group : {_id : "$by_user", num_tutorial : {$sum : "$likes"}}}])
db.mycol.aggregate([{$group : {_id : "$by_user", num_tutorial : {$avg : "$likes"}}}]

#delete a key : db.loginspect.update({}, {$unset: {custom_title_name:1}}, false, true)
    	



# where status equals either "A" or "D":
	> db.students.find( { address: { $in: [ "Sanepa", "Jhamsikhel" ] } } )
	
# SELECT user_id, status FROM users
	> db.users.find( { }, { user_id: 1, status: 1, _id: 0 } )	

# SELECT * FROM users WHERE status != "A"
	> db.users.find( { status: { $ne: "A" } }  )

# SELECT * FROM users WHERE status = "A" OR age = 50
	> db.users.find( { $or: [ { status: "A" } , { age: 50 } ] }  )

# SELECT * FROM users WHERE age > 25
	> db.users.find( { age: { $gt: 25 } }  )

### SELECT * FROM users WHERE age < 25
	> db.users.find( { age: { $lt: 25 } } )

# SELECT * FROM users WHERE age > 25 AND   age <= 50
	> db.users.find( { age: { $gt: 25, $lte: 50 } } )

# SELECT * FROM users WHERE user_id like "%bc%" 
	> db.users.find( { user_id: /bc/ } )

# SELECT * FROM users WHERE user_id like "bc%"
	> db.users.find( { user_id: /^bc/ } )

# SELECT * FROM users WHERE status = "A" ORDER BY user_id ASC
	> db.users.find( { status: "A" } ).sort( { user_id: 1 } )

# SELECT * FROM users WHERE status = "A" ORDER BY user_id DESC
	> db.users.find( { status: "A" } ).sort( { user_id: -1 } )

# SELECT COUNT(user_id) FROM users
	> db.users.count( { user_id: { $exists: true } } )
	> db.users.find( { user_id: { $exists: true } } ).count()

# SELECT COUNT(*) FROM users WHERE age > 30
	> db.users.count( { age: { $gt: 30 } } )
	
# SELECT DISTINCT(status) FROM users
	> db.users.distinct( "status" )

# SELECT * FROM users LIMIT 1
	> db.users.find().limit(1)

# SELECT * FROM users LIMIT 5 SKIP 10
	> db.users.find().limit(5).skip(10)
			
				








