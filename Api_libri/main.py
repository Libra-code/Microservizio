from flask import Flask, app 
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
api = Api(app)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///databse.db'
#crea il database nella stessa cartella dove lo usi

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8'.format(
    **{
      'user': os.getenv('DB_USER', 'root'),
      'password': os.getenv('DB_PASSWORD', 'root'),
      'host': os.getenv('DB_HOST', 'db'),
      'database': os.getenv('DB_DATABASE', 'db_01'),
    })
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = False

db = SQLAlchemy(app)

class BookModel(db.Model):
    """docstring for ClassName"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Book(title = {title},author = {author},genre = {genre})"
        

db.create_all()
#comando che va usato solo la prima volta poiche senno riscriverebbe di continuo il db

book_post_args = reqparse.RequestParser()
book_post_args.add_argument("title", type=str, help ="Title of the book is required", required=True)
book_post_args.add_argument("author", type=str, help="Author of the book is required", required=True)
book_post_args.add_argument("genre", type=str, help ="Genre on the book is required", required=True)
#aggiungendo required = true si rendono obbligatori gli argomenti


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
   
   @marshal_with(resource_fields)
    def delete(self, book_id):
        args = book_update_args.parse_args()
        result = BookModel.query.filter_by(id=book_id).first()
        if not result:
            abort(404, message = "Could not find book with that id")
        del result
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
