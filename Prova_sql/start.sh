#!/bin/sh 
sudo docker pull mysql/mysql-server:latest
sudo docker images
sudo docker run --name=[database_api] -d [database_api]
docker ps
apt-get install mysql-client
sudo docker logs [database_api]
sudo docker logs mysql_docker
sudo docker exec -it [database_api] bash
sudo docker -it mysql_docker bash
mysql> ALTER USER 'root'@'localhost' IDENTIFIED BY '[newpassword]';
sudo mkdir -p /root/docker/[container_name]/conf.d
sudo nano /root/docker/[container_name]/conf.d/my-custom.cnf
docker run \
--detach \
--name=[container_name] \
--env="MYSQL_ROOT_PASSWORD=[my_password]" \
--publish 6603:3306 \
--volume=/root/docker/[container_name]/conf.d:/etc/mysql/conf.d \
mysql
mysql -uroot -pmypassword -h127.0.0.1 -P6603 -e 'show global variables like "max_connections"';
sudo docker inspect [container_name]
sudo mkdir -p /storage/docker/mysql-data
docker run \
--detach \
--name=[container_name] \
--env="MYSQL_ROOT_PASSWORD=my_password" \
--publish 6603:3306 \
--volume=/root/docker/[container_name]/conf.d:/etc/mysql/conf.d \
--volume=/storage/docker/mysql-data:/var/lib/mysql \
mysql