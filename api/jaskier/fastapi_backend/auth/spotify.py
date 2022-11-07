import spotipy

from dotenv import load_dotenv
from os import environ


# load environment variables
load_dotenv('/Users/artempavlenko/PycharmProjects/phorminx/api/.env')

CLIENT_ID = environ.get('CLIENT_ID')
CLIENT_SECRET = environ.get('CLIENT_SECRET')
REDIRECT_URI = environ.get('REDIRECT_URI')
current_song_scope = environ.get('SCOPE_CURRENT_SONG')

spotifyOAuth = spotipy.SpotifyOAuth(client_id=CLIENT_ID,
                                    client_secret=CLIENT_SECRET,
                                    redirect_uri=REDIRECT_URI,
                                    scope=current_song_scope)

token = spotifyOAuth.get_access_token()

SP = spotipy.Spotify(auth=token['access_token'])


def get_sp():
    return SP


def refresh_token():
    global SP
    print("-----\n** start refreshing token **")
    token_info = spotifyOAuth.get_cached_token()
    token_info = spotifyOAuth.refresh_access_token(token_info['refresh_token'])
    token = token_info['access_token']
    SP = spotipy.Spotify(auth=token)
    print("-----\n** complete refreshing token **")
    return SP
