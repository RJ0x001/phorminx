import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware import Middleware

from jaskier.functions import run_lyrics_search

# TODO fix cors hosts
middleware = [Middleware(CORSMiddleware,
                         allow_origins=['*'],
                         allow_credentials=True,
                         allow_methods=['*'],
                         allow_headers=['*'])]

app = FastAPI(middleware=middleware)


@app.post("/user/", response_model=User)
def create_user(user: User):
    return user

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
