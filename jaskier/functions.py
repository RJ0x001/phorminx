import spotipy
import math

from time import sleep

from utils.token import get_spotipy_token, get_genius_obj
from config.config import scope_song


def get_song():
    username, token = get_spotipy_token(scope_song)
    spotipy_object = spotipy.Spotify(auth=token)
    current_song_spotify_obj = spotipy_object.current_user_playing_track()
    progress = current_song_spotify_obj['progress_ms']
    full_duration = current_song_spotify_obj['item']['duration_ms']
    next_track_time = math.ceil((full_duration - progress) / 1000)
    spotify_artist = current_song_spotify_obj['item']['album']['artists'][0]['name']
    spotify_song = current_song_spotify_obj['item']['name']
    return spotify_artist, spotify_song, next_track_time


def get_lyrics(artist, song):
    genius = get_genius_obj()
    lyrics = genius.search_song(song, artist)
    try:
        return lyrics.lyrics
    except AttributeError:
        return 'Not found'


def run_lyrics_search():
    while True:
        artist, song, next_track_time = get_song()
        lyrics = get_lyrics(artist, song)
        print(artist, song, '\n', lyrics, '\n', 'sleeping %s seconds' % next_track_time)
        sleep(next_track_time)
