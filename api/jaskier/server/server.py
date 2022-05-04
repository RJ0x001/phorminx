import secrets
import string
from os import environ, getenv

from flask import (
    abort,
    Flask,
    make_response,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

from dotenv import load_dotenv


from flask_restful import Api, Resource, reqparse
from flask_cors import CORS, cross_origin
from flask_login import LoginManager
from urllib.parse import urlencode

from .handlers import LyricsApiHandler

app = Flask(__name__)
api = Api(app)
cors = CORS(app)
login_manager = LoginManager()
login_manager.init_app(app)

api.add_resource(LyricsApiHandler, '/jaskier/lyrics/')

# Client info
CLIENT_ID = environ.get('CLIENT_ID')
CLIENT_SECRET = environ.get('CLIENT_SECRET')
REDIRECT_URI = environ.get('REDIRECT_URI')

# load environment variables
load_dotenv('/Users/artempavlenko/PycharmProjects/phorminx/api/.env')

# Spotify API endpoints
AUTH_URL = 'https://accounts.spotify.com/authorize'
TOKEN_URL = 'https://accounts.spotify.com/api/token'
ME_URL = 'https://api.spotify.com/v1/me'


@app.route('/<loginout>')
def login(loginout):
    '''Login or logout user.
    Note:
        Login and logout process are essentially the same. Logout forces
        re-login to appear, even if their token hasn't expired.
    '''

    # redirect_uri can be guessed, so let's generate
    # a random `state` string to prevent csrf forgery.
    state = ''.join(
        secrets.choice(string.ascii_uppercase + string.digits) for _ in range(16)
    )

    # Request authorization from user
    scope = 'user-read-private user-read-email'

    if loginout == 'logout':
        payload = {
            'client_id': CLIENT_ID,
            'response_type': 'code',
            'redirect_uri': REDIRECT_URI,
            'state': state,
            'scope': scope,
            'show_dialog': True,
        }
    elif loginout == 'login':
        payload = {
            'client_id': CLIENT_ID,
            'response_type': 'code',
            'redirect_uri': REDIRECT_URI,
            'state': state,
            'scope': scope,
        }
    else:
        abort(404)

    res = make_response(redirect(f'{AUTH_URL}/?{urlencode(payload)}'))
    res.set_cookie('spotify_auth_state', state)

    return res
