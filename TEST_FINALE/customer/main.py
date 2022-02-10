#!/usr/bin/python 
from flask import Flask,request,jsonify,json
from flask_pymongo import PyMongo
from flask_restful import reqparse , Resource , Api
import pymongo


app = Flask(__name__)
api = Api(app)

app.config['MONGO_DBNAME'] = 'library_db'
app.config['MONGO_URI'] = 'mongodb://flask_app_customer_db/library_db'
mongo = PyMongo(app)


customer = mongo.db.library_db
#indice per usarlo come parametro
customer.create_index([('user_id', pymongo.ASCENDING)],unique=True)

def make_json(j):
  return json.loads(json.dumps(j))


class Costumer(Resource):
  def get_one_customer(user_id):
    c = customer.find_one({'user_id' : user_id})
    if c:
      c["_id"]=str(c['_id'])
      output=(make_json(c))  
    else:
      output = "No such user"
    return jsonify({'result' : output})

  def add_customer():
    user_id = request.json['user_id']
    c = customer.find_one({'user_id': user_id})
    if c:
      output = "Already exists"
    else:
      new_customer = customer.insert_one(make_json((request.json)))
      output = make_json((request.json))
    return jsonify({'result' : output})

  def delete_one_customer(user_id):
    c = customer.find_one({'user_id': user_id})
    if c:
      customer.delete_one({'user_id': user_id})
      output = "Successfully deleted"
    else:
      output = "No such user"
    return jsonify({'result' : output})
 
  def change_one_customer(user_id):
    c = customer.find_one({'user_id': user_id})
    if c:
      customer.delete_one({'user_id': user_id})
      new_customer = customer.insert_one(make_json((request.json)))
      output = make_json((request.json))
    else:
      output = "No such title"
    return jsonify({'result' : output})

api.add_resource(Costumer, "/customer/<int:user_id>")

class Get_all(Resource):
  def get_all_customers():
        output = []
        all_customer=customer.find()
        if all_customer:
          for c in all_customer: 
            c["_id"]=str(c['_id'])
            output.append(make_json(c)) 
        else:
          output = "No user"  
        return jsonify({'result' : output})


api.add_resource(Get_all, "/customer")



#end of code to run it
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=False)