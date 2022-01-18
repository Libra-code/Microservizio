import datetime
from xmlrpc.client import DateTime
import mysql.connector
from flask import jsonify
import json
from datetime import datetime

#convert result from sql to json
def to_json(myresult):
  customer_all=[]
  for x in myresult:
    myjson3 = {
                'borrowing_id': x[0],
                'book_id': x[1],
                'customer_id': x[2] ,
                'start_date': str(x[3])                
            }
    customer_all.append(myjson3)
  customer_all_json= f'{{"results": {json.dumps(customer_all)}}}'
  print (customer_all_json)
  #return(jsonify(customer_all_json))

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="db_01"
)

mycursor = mydb.cursor()
try:
  mycursor.execute("CREATE TABLE borrowing (borrowing_id int AUTO_INCREMENT, book_id VARCHAR(255) NOT NULL , customer_id VARCHAR(255) NOT NULL, start_date DATETIME, PRIMARY KEY (borrowing_id))")
  print("Create table 'borrowing' successful")
except:
  print("Table 'borrowing' already exists")



def post():
  now = datetime.now()
  formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')

  sql = "INSERT INTO borrowing (book_id, customer_id, start_date) VALUES (%s, %s, %s)"
  val = ("Hall", "Highway", formatted_date)
  mycursor.execute(sql, val)
  mydb.commit()
  print(mycursor.rowcount, "record inserted.")

def get():

  print("get:")
  mycursor.execute("SELECT * FROM borrowing")
  myresult = mycursor.fetchall()
  print(to_json(myresult))

def getLast():
  print("get:")
  mycursor.execute("SELECT * FROM customer ORDER BY customer_id DESC LIMIT 1")
  myresult = mycursor.fetchall()
  print(to_json(myresult))
  
#post()
get()
#getLast()






