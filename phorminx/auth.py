import spotipy.util as util


from .config import USER, client_id, client_secret, redirect_uri, scope


def get_spotipy_token(scope):
    """
    Token for auth ob Spotify
    """
    token = util.prompt_for_user_token(USER, scope, client_id, client_secret, redirect_uri)
    return USER, token
