from datetime import date, datetime
from flask import Flask, app 
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
api = Api(app)

#crea il database nella stessa cartella dove lo usi
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///databse.db'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8'.format(
    **{
      'user': os.getenv('DB_USER', 'root'),
      'password': os.getenv('DB_PASSWORD', 'root'),
      'host': os.getenv('DB_HOST', 'db_borrowing'),
      'database': os.getenv('DB_DATABASE', 'db_01'),
    })
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False

db = SQLAlchemy(app)

class BorrowingModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, nullable=False)
    costumer_id = db.Column(db.Integer, nullable=False)
    due_date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"Borrowing(book_id = {self.book_id},costumer_id = {self.costumer_id},genre = {self.due_date})"
        

db.create_all()
#comando che va usato solo la prima volta poiche senno riscriverebbe di continuo il db

borrowing_post_args = reqparse.RequestParser()
borrowing_post_args.add_argument("book_id", type=int, help ="ID of the book borrowed is required", required=True)
borrowing_post_args.add_argument("costumer_id", type=int, help="ID of the costumer borrowing is required", required=True)
borrowing_post_args.add_argument("due_date", type=datetime, help ="Due date of the borrow is required", required=True)
#aggiungendo required = true si rendono obbligatori gli argomenti

#usando il patch non sono necessari tutti i campi
borrowing_update_args = reqparse.RequestParser()
borrowing_update_args.add_argument("book_id", type=int, help ="ID of the book borrowed")
borrowing_update_args.add_argument("costumer_id", type=int, help ="ID of the costumer borrowing")
borrowing_update_args.add_argument("due_date", type=datetime, help ="Due date of the borrow")


resource_fields = {
    'id':fields.Integer,
    'book_id':fields.Integer,
    'costumer_id':fields.Integer,
    'due_date':fields.DateTime
}

class Borrowing(Resource):
    @marshal_with(resource_fields)
    def get(self, borrowing_id):
        result = BorrowingModel.query.filter_by(id=borrowing_id).first()
        if not result:
            abort(404, message = "Could not find with that id")
        return result
    
    
    @marshal_with(resource_fields)
    def post(self, borrowing_id):
        args = borrowing_post_args.parse_args()
        result = BorrowingModel.query.filter_by(id=borrowing_id).first()
        if result:
            abort(409, message = "borrowing id taken...")

        borrowing = BorrowingModel(id=borrowing_id, book_id=args['book_id'], costumer_id=args['costumer_id'],due_date=args['due_date'])
        db.session.add(borrowing)
        db.session.commit()
        return borrowing, 201


    @marshal_with(resource_fields)
    def patch(self ,borrowing_id):
        args = borrowing_update_args.parse_args()
        result = BorrowingModel.query.filter_by(id=borrowing_id).first()
        if not result:
            abort(404, message = "Could not find with that id")
        if args['book_id']:
            result.book_id = args['book_id']
        if args['costumer_id']:
            result.costumer_id = args['costumer_id']
        if args['due_date']:
            result.due_date = args['due_date']
        #il parser mette tutto quello che non è presente come =none

        db.session.commit()
        return result
   

    def delete(self, borrowing_id):
        args = borrowing_update_args.parse_args()
        result = BorrowingModel.query.filter_by(id=borrowing_id).first()
        if not result:
            abort(404, message = "Could not find borrowing with that id")
        del result
        return '', 204


api.add_resource(Borrowing, "/borrowing/<int:borrowing_id>")

class Get_all(Resource):
        @marshal_with(resource_fields)
        def get(self):
                result = BorrowingModel.query.all()
                if not result:
                    abort(404, message = "Could not find anything")
                return result

api.add_resource(Get_all, "/borrowing")

#end of code to run it
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=False)