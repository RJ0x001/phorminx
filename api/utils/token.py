import spotipy.util as util
from lyricsgenius import Genius

from api.utils.config import USER, client_id, client_secret, redirect_uri, genius_token


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
