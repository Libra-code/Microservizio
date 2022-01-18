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


class VideoModel(db.Model):
    """docstring for ClassName"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Video(name = {name},views = {views},likes = {likes})"
        

#db.create_all()
#comando che va usato solo la prima volta poiche senno riscriverebbe di continuo il db

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required", required=True)
video_put_args.add_argument("views", type=int, help="Views of the video is required", required=True)
video_put_args.add_argument("likes", type=int, help="Likes on the video is required", required=True)
#aggiungendo required = true si rendono obbligatori gli argomenti


video_update_args = reqparse.RequestParser()
video_update_args.add_argument("name", type=str, help="Name of the video")
video_update_args.add_argument("views", type=int, help="Views of the video")
video_update_args.add_argument("likes", type=int, help="Likes on the video")


resource_fields = {
    'id':fields.Integer,
    'name':fields.String,
    'views':fields.Integer,
    'likes':fields.Integer
}

class Video(Resource):
    @marshal_with(resource_fields)
    def get(self, video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message = "Could not find video with that id")
        return result
    
    
    @marshal_with(resource_fields)
    def put(self, video_id):
        args = video_put_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if result:
            abort(409, message = "Video id taken...")

        video = VideoModel(id=video_id, name=args['name'], views=args['views'],likes=args['likes'])
        db.session.add(video)
        db.session.commit()
        return video, 201


    @marshal_with(resource_fields)
    def patch(self ,video_id):
        args = video_update_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message = "Could not find video with that id")
        if args['name'] :
            result.name = args['name']
        if args['views']:
            result.views = args['views']
        if args['likes']:
            result.likes = args['likes']
        #il parser mette tutto quello che non è presente come =none

        db.session.commit()
        return result



    def delete(self, video_id):
        args = video_update_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message = "Could not find video with that id")
        del result
        return '', 204


api.add_resource(Video, "/video/<int:video_id>")

class Get_all(Resource):
        @marshal_with(resource_fields)
        def get(self):
                result = VideoModel.query.all()
                if not result:
                    abort(404, message = "Could not find videos")
                return result

api.add_resource(Get_all, "/video")


#end of code to run it
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=False)