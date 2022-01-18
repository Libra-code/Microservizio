from flask import Flask, url_for, request,jsonify,json
from flask_pymongo import PyMongo

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
  return jsonify({'result' : output})

@app.route('/book/<name>', methods=['GET'])
def get_one_book(name):
  print(name)
  book = mongo.db.library_db
  b = book.find_one({'name' : name})
  if b:
    b["_id"]=str(b['_id'])
    output=(make_json(b))  
  else:
    output = "No such name"
  return jsonify({'result' : output})

#@app.route('/book/<>', methods=['GET'])
#def get_collectiom(collection):
  where = request.args.get('where')
  if where:
    args['spec'] = json.loads(where)
    response = {}
    documents = []
    
  cursor = db(collection).find(**args)
  for document in cursor:
    documents.append(document)
  
  response[collection] = documents
  return (response)

@app.route('/book', methods=['POST'])
def add_book():
  book = mongo.db.library_db
  name = request.json['name']
  #serve il json con il nome
  b = book.find_one({'name': name})
  if b:
    output = "Already exists"
  else:
    new_book = book.insert(make_json((request.json)))
    output = make_json((request.json))
  return jsonify({'result' : output})

@app.route('/book/<name>', methods=['DELETE'])
def delete_one_book(name):
  book = mongo.db.library_db
  #non serve il json con il nome
  #il nome va messo nell'url
  b = book.find_one({'name': name})
  if b:
    book.delete_one({'name': name})
    output = "Successfully deleted"
  else:
    output = "No such name"
  return jsonify({'result' : output})

@app.route('/book/<name>', methods=['PUT'])
def change_one_book(name):
  book = mongo.db.library_db
  b = book.find_one({'name': name})
  if b:
    book.delete_one({'name': name})
    new_book = book.insert(make_json((request.json)))
    output = make_json((request.json))
  else:
    output = "No such name"
  return jsonify({'result' : output})


#end of code to run it
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)
