import uvicorn
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware import Middleware
import spotipy.util as util

from jaskier.functions import run_lyrics_search


# TODO fix cors hosts
middleware = [Middleware(CORSMiddleware,
                         allow_origins=['*'],
                         allow_credentials=True,
                         allow_methods=['*'],
                         allow_headers=['*'])]

app = FastAPI(middleware=middleware)


# @app.post("/user/", response_model=User)
# def create_user(user: User):
#     return user


@app.get('/jaskier/user')
def user_auth():
    CLIENT_ID = "5b5a6bb841554aa6ba269f2a690bb3d0"
    CLIENT_SECRET = "a96b2d0d248443ffa18cd3c0349b4511"
    REDIRECT_URI = "http://localhost:8888/callback/"
    USERNAME = os.getenv('USERNAME')
    scope = 'user-library-read'
    token = util.prompt_for_user_token(
        username=USERNAME,
        scope=scope,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI)
    print(token)


@app.get('/jaskier/lyrics/')
async def lyrics():
    res = run_lyrics_search()
    return {
        'resultStatus': 'SUCCESS',
        'artist': res["artist"],
        'song': res["song"],
        'lyrics': res["lyrics"],
        'artist_img': res['artist_img'],
        'album_title': res['album_title'],
        'timeLeft': res["next_track"],
    }
