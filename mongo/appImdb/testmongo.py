import export
from pymongo import MongoClient
import pymongo
import bson.json_util



client = pymongo.MongoClient("mongodb://ste:SalopTRE@cluster0-shard-00-00.vh9ph.mongodb.net:27017,cluster0-shard-00-01.vh9ph.mongodb.net:27017,cluster0-shard-00-02.vh9ph.mongodb.net:27017/MDB?ssl=true&replicaSet=atlas-104rkc-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test

mydb = client["MDB"]

mycol = mydb["Film"]

mydict = { "name": "John", "address": "Highway 37" }

x = mycol.insert_one(mydict)



'''client = pymongo.MongoClient("mongodb://ty:3oaIPm0q8MqSgXek@cluster0.8i6v0.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")


#client = pymongo.MongoClient("mongodb+srv://ty:3oaIPm0q8MqSgXek@cluster0.8i6v0.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test

mydb = client["myFirstDatabase"]

mycol = mydb["movie"]


for x in mycol.find():
  print(x)'''