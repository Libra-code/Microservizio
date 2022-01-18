from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
from flask import json

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'library_db'
app.config['MONGO_URI'] = 'mongodb://db/library_db'

mongo = PyMongo(app)

def make_json(j):
  return json.loads(json.dumps(j))

@app.route('/book', methods=['GET'])
def get_all_books():
  book = mongo.db.library_db
  output = []
  for b in book.find(): 
    b["_id"]=str(b['_id'])
    output.append(make_json(b))

  print("GET succes")  
  return jsonify({'result' : output})

@app.route('/book/<title>', methods=['GET'])
def get_one_book(title):
  print(title)
  book = mongo.db.library_db
  b = book.find_one({'title' : title})
  if b:
    b["_id"]=str(b['_id'])
    output=(make_json(b))  
  else:
    output = "No such title"
  return jsonify({'result' : output})

@app.route('/book', methods=['POST'])
def add_book():
  book = mongo.db.library_db
  title = request.json['title']
  #serve il json con il title
  b = book.find_one({'title': title})
  if b:
    output = "Already exists"
  else:
    new_book = book.insert_one(make_json((request.json)))
    output = make_json((request.json))
  return jsonify({'result' : output})

@app.route('/book/<title>', methods=['DELETE'])
def delete_one_book(title):
  book = mongo.db.library_db
  #non serve il json con il nome
  #il nome va messo nell'url
  b = book.find_one({'title': title})
  if b:
    book.delete_one({'title': title})
    output = "Successfully deleted"
  else:
    output = "No such title"
  return jsonify({'result' : output})


@app.route('/book/<title>', methods=['PUT'])
def change_one_book(title):
  book = mongo.db.library_db
  b = book.find_one({'title': title})
  if b:
    book.delete_one({'title': title})
    new_book = book.insert_one(make_json((request.json)))
    output = make_json((request.json))
  else:
    output = "No such title"
  return jsonify({'result' : output})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
    print("Microservice is ready")
    