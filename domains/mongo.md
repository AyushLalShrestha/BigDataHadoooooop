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

