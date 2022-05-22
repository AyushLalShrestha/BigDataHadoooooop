
Installing RabbitMQ:
1. echo "deb http://www.rabbitmq.com/debian/ testing main"  | sudo tee  /etc/apt/sources.list.d/rabbitmq.list > /dev/null
2. wget https://www.rabbitmq.com/rabbitmq-signing-key-public.asc
3. sudo apt-key add rabbitmq-signing-key-public.asc
4. sudo apt-get update
5. sudo apt-get install rabbitmq-server -y
6. sudo service rabbitmq-server start
7. sudo rabbitmq-plugins enable rabbitmq_management
8. sudo service rabbitmq-server restart

Customizing User in RabbitMQ:
1. sudo rabbitmqctl add_user rabbituser rabbitpass
2. sudo rabbitmqctl set_user_tags rabbituser administrator
3. sudo rabbitmqctl set_permissions -p / rabbituser ".*" ".*" ".*"
4. to delete guest user please run this command `sudo rabbitmqctl delete_user guest`

Installing ampq-tools:
1. sudo apt-get update -y
2. sudo apt-get install -y amqp-tools