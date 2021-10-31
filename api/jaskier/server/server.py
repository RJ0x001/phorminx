from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS, cross_origin

from .handlers import LyricsApiHandler

app = Flask(__name__)
api = Api(app)
cors = CORS(app)
api.add_resource(LyricsApiHandler, '/jaskier/lyrics/')

