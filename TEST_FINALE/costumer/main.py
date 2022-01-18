from flask import Flask,request,jsonify,json
from flask_pymongo import PyMongo
from flask_restful import reqparse
import pymongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'library_db'
app.config['MONGO_URI'] = 'mongodb://flask_app_costumer_db/library_db'

mongo = PyMongo(app)
costumer = mongo.db.library_db
costumer.create_index([('user_id', pymongo.ASCENDING)],unique=True)


def make_json(j):
  return json.loads(json.dumps(j))

@app.route('/costumer', methods=['GET'])
def get_all_costumers():
  output = []
  all_costumer=costumer.find()
  if all_costumer:
    for c in all_costumer: 
      c["_id"]=str(c['_id'])
      output.append(make_json(c)) 
  else:
    output = "No user"  
  return jsonify({'result' : output})

@app.route('/costumer/<user_id>', methods=['GET'])
def get_one_costumer(user_id):
  c = costumer.find_one({'user_id' : user_id})
  if c:
    c["_id"]=str(c['_id'])
    output=(make_json(c))  
  else:
    output = "No such user"
  return jsonify({'result' : output})

@app.route('/costumer', methods=['POST'])
def add_costumer():
  user_id = request.json['user_id']
  c = costumer.find_one({'user_id': user_id})
  if c:
    output = "Already exists"
  else:
    new_costumer = costumer.insert_one(make_json((request.json)))
    output = make_json((request.json))
  return jsonify({'result' : output})

@app.route('/costumer/<user_id>', methods=['DELETE'])
def delete_one_costumer(user_id):
  c = costumer.find_one({'user_id': user_id})
  if c:
    costumer.delete_one({'user_id': user_id})
    output = "Successfully deleted"
  else:
    output = "No such user"
  return jsonify({'result' : output})
 


@app.route('/costumer/<user_id>', methods=['PUT'])
def change_one_costumer(user_id):
  c = costumer.find_one({'user_id': user_id})
  if c:
    costumer.delete_one({'user_id': user_id})
    new_costumer = costumer.insert_one(make_json((request.json)))
    output = make_json((request.json))
  else:
    output = "No such title"
  return jsonify({'result' : output})

#end of code to run it
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=False)