import spotipy
import math
import pprint
from utils.config import scope_song, get_spotipy_token, get_genius_obj

TRASH_COMP = ('live', 'explicit', 'remaster', 'bonus track')


def get_song():
    username, token = get_spotipy_token(scope_song)
    spotipy_object = spotipy.Spotify(auth=token)
    current_song_spotify_obj = spotipy_object.current_user_playing_track()
    progress = current_song_spotify_obj['progress_ms']
    full_duration = current_song_spotify_obj['item']['duration_ms']
    next_track_time = math.ceil((full_duration - progress) / 1000)
    spotify_artist = current_song_spotify_obj['item']['album']['artists'][0]['name']
    album_title = current_song_spotify_obj['item']['album']['images'][0]['url']
    artist_raw = spotipy_object.search(q='artist:' + spotify_artist, type='artist')
    artist_img = artist_raw['artists']['items'][0]['images'][0]['url']
    spotify_song = current_song_spotify_obj['item']['name']
    return spotify_artist, spotify_song, artist_img, album_title, next_track_time


def clear_title(song):
    for trash in TRASH_COMP:
        if trash in song.lower():
            song = song.lower().split(trash)[0]
            i = 0
            for x in song[::-1]:
                if not x.isalpha():
                    i += 1
                else:
                    break
            song = song[:-i]
    return song


def get_lyrics(artist, song, next_track_time):
    result_dict = {
        "artist": artist,
        "song": song,
        "next_track": next_track_time,
        "lyrics": None
    }
    if any(trash in song.lower() for trash in TRASH_COMP):
        song = clear_title(song)
    genius = get_genius_obj()
    lyrics = genius.search_song(song, artist)
    try:
        result_dict["lyrics"] = lyrics.lyrics
    except AttributeError:
        result_dict["lyrics"] = "Не удалось найти текст :("
    return result_dict


def run_lyrics_search():
    artist, song, artist_img, album_title, next_track_time = get_song()
    result = get_lyrics(artist, song, next_track_time)
    result['artist_img'] = artist_img
    result['album_title'] = album_title
    return result
