import export
from pymongo import MongoClient
import pymongo
import bson.json_util


#python version 2.7.18

client = pymongo.MongoClient("mongodb://ty:3oaIPm0q8MqSgXek@cluster0-shard-00-00.8i6v0.mongodb.net:27017,cluster0-shard-00-01.8i6v0.mongodb.net:27017,cluster0-shard-00-02.8i6v0.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-xcsu95-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test
mydb = client["myFirstDatabase"]
mycol = mydb["test"]

for i in export.actorsForImport:
 x = mycol.insert_one(bson.json_util.loads(i))


