Apache kafka : Kafka Setup for Pseudo distributed

# simple command line produce and consume
1. start the kafka broker service via ./bin/kafka-server-start.sh -daemon config/server.properties
2. ./kafka-topics.sh --create --zookeeper ayushUbuntu:2181 --replication-factor 1 --partitions 1 --topic log-test
3. ./kafka-topics.sh --list --zookeeper ayushUbuntu:2181
4. ./kafka-console-producer.sh --broker-list ayushUbuntu:9092 --topic log-test
5. ./kafka-console-consumer.sh --bootstrap-server ayushUbuntu:9092 --topic ayush --zookeeper localhost:2181


# consuming and producing from a file
1. ./bin/kafka-server-start.sh -daemon config/server.properties
1. vi connect-standalone.properties
	->    bootstrap.servers=ayushUbuntu:9092

2. vi connect-file-source.properties
	->    file=/tmp/webserver_access.log
	      topic=log_test		

3. vi connect-file-sink
	->    file=/home/ayushshr/webserver_log_output.txt
	      topics=log_test		

4. ./bin/connect-standalone.sh ./config/connect-standalone.properties ./config/connect-file-source.properties ./config/connect-file-sink.properties

5. ./kafka-console-consumer.sh --bootstrap-server ayushUbuntu:9092 --topic log-test --from-beginning	


# custom zookeeper start (before starting kafka broker)
  ./bin/zookeeper-server-start.sh -daemon config/zookeeper.properties
