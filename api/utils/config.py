import spotipy.util as util
from lyricsgenius import Genius


USER = 'rj0x001'
client_id = "5b5a6bb841554aa6ba269f2a690bb3d0"
client_secret = "a96b2d0d248443ffa18cd3c0349b4511"
redirect_uri = "http://localhost:8888/callback/"
scope = ("playlist-read-private "
         "playlist-modify-private "
         "playlist-modify-public "
         "playlist-read-collaborative ")

scope_song = (
              "user-read-currently-playing"
              )

genius_token = 'oq18Ynk0MDUqUO2PGKXqTxLH82-7ji9diIvTu-FpRmX7fNvMeFo5klHMnohURYUb'


def get_spotipy_token(scope):
    """
    Token for auth ob Spotify
    """
    token = util.prompt_for_user_token(USER, scope, client_id, client_secret, redirect_uri)
    return USER, token


def get_genius_obj():
    """
    Get genius object
    :return:
    """
    genius = Genius(genius_token)
    return genius
