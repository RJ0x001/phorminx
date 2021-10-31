import os

from flask import Flask, render_template
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS, cross_origin

from .handlers import LyricsApiHandler


# template_dir = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
# template_dir = os.path.join(template_dir, 'templates')
app = Flask(__name__)
api = Api(app)
cors = CORS(app)
api.add_resource(LyricsApiHandler, '/jaskier/lyrics/')

