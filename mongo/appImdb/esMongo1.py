import export
from pymongo import MongoClient
import pymongo
import bson.json_util
import ssl
import certifi
ca = certifi.where()
#https://stackoverflow.com/questions/54484890/ssl-handshake-issue-with-pymongo-on-python3
#python version 3.9.0

client = pymongo.MongoClient("mongodb+srv://ste:SalopTRE@cluster0.vh9ph.mongodb.net/MDB?retryWrites=true&w=majority", tlsCAFile=ca)
db = client.test
mydb = client["MDB"]
mycol = mydb["Actors"]

#for i in export.actorsForImport:
# x = mycol.insert_one(bson.json_util.loads(i))

x = mycol.delete_one({"nconst": "nm0000001"})