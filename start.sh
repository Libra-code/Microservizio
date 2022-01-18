#!/bin/sh 
#comandi lab 6
helm repo add bitnami https://charts.bitnami.com/bitnami
helm install --values kafka-values.yaml kafka bitnami/kafka 
helm repo add elastic https://helm.elastic.co
helm install --values elasticsearch-values.yaml elasticsearch elastic/
helm install --values logstash-values.yaml logstash elastic/logstash
helm install --values filebeat-values.yaml filebeat elastic/filebeat
helm install --values kibana-values.yaml kibana elastic/kibana
helm install --values mongodb-values.yaml customer-mongodb bitnami/mongodb
helm install --values postgresql-values.yaml order-postgres bitnami/
kubectl run order-postgres-client --rm --tty -i --restart='Never' --namespace default --image docker.io/bitnami/postgresql:11.10.0-debian-10-r24 --env="PGPASSWORD=postgres" --command -- psql --host order-postgres -U postgres -d postgres -p 5432