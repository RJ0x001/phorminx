import logging
from typing import List, Union
import inspect

from os import environ
import spotipy
import requests
from dotenv import load_dotenv
from fastapi import FastAPI, APIRouter


from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware

from auth.spotify import get_sp, refresh_token

from lyrics.genius import get_lyrics
from lyrics.utils import get_time_fot_next_track, no_song_response, no_connection_exception

from routers import users

middleware = [Middleware(CORSMiddleware,
                         allow_origins=['http://localhost:3000'],
                         allow_credentials=True,
                         allow_methods=['GET'],
                         allow_headers=['*'])]

app = FastAPI(middleware=middleware)

app.include_router(users.router)


@app.get("/jaskier/lyrics/")
async def lyrics_search():
    sp = get_sp()

    try:
        current_song_spotify_obj = sp.current_user_playing_track()
    except requests.exceptions.ConnectionError:
        return no_connection_exception()

    except spotipy.exceptions.SpotifyException as e:
        sp = refresh_token()
        current_song_spotify_obj = sp.current_user_playing_track()

    if not current_song_spotify_obj:
        return no_song_response()

    try:
        next_track_time = get_time_fot_next_track(current_song_spotify_obj['progress_ms'],
                                                  current_song_spotify_obj['item']['duration_ms'])

    except TypeError:
        return no_song_response(30)

    spotify_artist = current_song_spotify_obj['item']['album']['artists'][0]['name']
    album_title = current_song_spotify_obj['item']['album']['images'][0]['url']
    artist_raw = sp.search(q='artist:' + spotify_artist, type='artist')

    # TODO default artist image
    try:
        artist_img = artist_raw['artists']['items'][0]['images'][0]['url']
    except IndexError:
        artist_img = ''

    spotify_song = current_song_spotify_obj['item']['name']
    res = get_lyrics(spotify_artist, spotify_song)
    res['artist_img'] = artist_img
    res['album_title'] = album_title
    res['next_track'] = next_track_time

    return res


@app.get("/health")
async def get_health():
    return {"message": "OK"}
