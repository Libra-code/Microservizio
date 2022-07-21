#!/usr/bin/python 
from flask import Flask, app 
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine


app = Flask(__name__)
api = Api(app)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///databse.db'
#crea il database nella stessa cartella dove lo usi

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@flask_app_books_db/db_01'
engine = create_engine('mysql+pymysql://root:root@flask_app_books_db/db_01')
db     = SQLAlchemy(app)

class BookModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Book(title = {self.title},author = {self.author},genre = {self.genre})"
    #The class defines a __repr__() method,it's optional is used to nicely formatted objects

db.create_all()


book_post_args = reqparse.RequestParser()
book_post_args.add_argument("title", type=str, help ="Title of the book is required", required=True)
book_post_args.add_argument("author", type=str, help="Author of the book is required", required=True)
book_post_args.add_argument("genre", type=str, help ="Genre on the book is required", required=True)
#aggiungendo required = true si rendono obbligatori gli argomenti

#usando il patch non sono necessari tutti i campi
book_update_args = reqparse.RequestParser()
book_update_args.add_argument("title", type=str, help ="Title of the book")
book_update_args.add_argument("author", type=str, help ="Author of the book")
book_update_args.add_argument("genre", type=str, help ="Genre on the book")


resource_fields = {
    'id':fields.Integer,
    'title':fields.String,
    'author':fields.String,
    'genre':fields.String
}

class Book(Resource):
    @marshal_with(resource_fields)
    def get(self, book_id):
        result = BookModel.query.filter_by(id=book_id).first()
        if not result:
            abort(404, message = "Could not find book with that id")
        return result
    
    
    @marshal_with(resource_fields)
    def post(self, book_id):
        args = book_post_args.parse_args()
        result = BookModel.query.filter_by(id=book_id).first()
        if result:
            abort(409, message = "book id taken...")

        book = BookModel(id=book_id, title=args['title'], author=args['author'],genre=args['genre'])
        db.session.add(book)
        db.session.commit()
        return book, 201


    @marshal_with(resource_fields)
    def patch(self ,book_id):
        args = book_update_args.parse_args()
        result = BookModel.query.filter_by(id=book_id).first()
        if not result:
            abort(404, message = "Could not find book with that id")
        if args['title']:
            result.title = args['title']
        if args['author']:
            result.author = args['author']
        if args['genre']:
            result.genre = args['genre']
        #il parser mette tutto quello che non è presente come =none

        db.session.commit()
        return result
   

    def delete(self, book_id):
        args = book_update_args.parse_args()
        result = BookModel.query.filter_by(id=book_id).first()
        if not result:
            abort(404, message = "Could not find book with that id")
        
        
        result = BookModel.query.filter_by(id=book_id).delete()
        db.session.commit()
        return '', 204


api.add_resource(Book, "/book/<int:book_id>")

class Get_all(Resource):
        @marshal_with(resource_fields)
        def get(self):
                result = BookModel.query.all()
                if not result:
                    abort(404, message = "Could not find books")
                return result

api.add_resource(Get_all, "/book")

#end of code to run it
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=False)
