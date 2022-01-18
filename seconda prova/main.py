from flask import Flask,request,jsonify,json
from flask_pymongo import PyMongo
from flask_restful import reqparse
import pprint
import pymongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'library_db'
app.config['MONGO_URI'] = 'mongodb://flask_app_costumer_db/library_db'

mongo = PyMongo(app)
mongo.db.library_db.costumer.create_index([('user_id', pymongo.ASCENDING)],unique=True)

costumer_post_args = reqparse.RequestParser()
costumer_post_args.add_argument("user_id", type=int, help ="The ID of the user is required", required=True)

def make_json(j):
  return json.loads(json.dumps(j))

#get all
@app.route('/costumer', methods=['GET'])
def get_all_costumers():
  costumer = mongo.db.library_db
  output = []
  for b in costumer.find(): 
      b["_id"]=str(b['_id'])
      output.append(make_json(b))
      print("GET succes")

  return jsonify({'result' : output})

#get one
@app.route('/costumer/<user_id>', methods=['GET'])
def get_one_book(user_id):
  
  costumer = mongo.db.library_db
  output = pprint.pprint(costumer.find_one({"user_id": f"{user_id}"}))
  if not output:
    output = "No such costumer"
      
  return jsonify({'result' : output,"id":f"{output.__inserted_id}",})    
      
@app.route('/costumer', methods=['POST'])
def add_costumer():
  args = costumer_post_args.parse_args()
  costumer = mongo.db.library_db
  output = costumer.find_one({"user_id": f"{args['user_id']}"})
  if output:
    output = "Already exists"
  else:
    new_costumer = costumer.insert_one(make_json(args))
    output = make_json(args)
  return jsonify({'result' : output})

@app.route('/costumer/<user_id>', methods=['DELETE'])
def delete_one_costumer(user_id):
  costumer = mongo.db.library_db
  #non serve il json con il nome
  #il nome va messo nell'url
  b = costumer.find_one({'user_id': user_id})
  if b:
    costumer.delete_one({'user_id': user_id})
    output = "Successfully deleted"
  else:
    output = "No such user_id"
  return jsonify({'result' : output})


@app.route('/book/<user_id>', methods=['PUT'])
def change_one_book(user_id):
  args = costumer_post_args.parse_args()
  costumer = mongo.db.library_db
  b = costumer.find_one({'user_id': user_id})
  if b:
    costumer.delete_one({'user_id': user_id})
    new_book = costumer.insert_one(make_json(args))
    output = make_json(args)
  else:
    output = "No such title"
  return jsonify({'result' : output})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
    print("Microservice is ready")