import requests

from lyricsgenius import Genius

from lyrics.utils import TRASH_COMP, clear_title, good_trash_lyrics
from config import GENIUS_TOKEN

genius = Genius(GENIUS_TOKEN)


def get_lyrics(artist, song):
    result_dict = {
            "artist": artist,
            "song": song,
            "lyrics": None
        }
    if any(trash in song.lower() for trash in TRASH_COMP):
        song = clear_title(song)

    # TODO clean URLCopyEmbedCopy trash

    try:
        lyrics = genius.search_song(song, artist)
    except requests.exceptions.Timeout:
        result_dict["lyrics"] = "Timeout error with genius"
        return result_dict

    if lyrics and good_trash_lyrics(lyrics.lyrics):
        result_dict["lyrics"] = lyrics.lyrics
    else:
        result_dict["lyrics"] = "Can't find the lyrics"

    return result_dict
