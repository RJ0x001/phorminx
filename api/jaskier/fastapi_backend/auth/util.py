import spotipy


def refresh(spotify_oauth, ):
	token_info = spotify_oauth.get_cached_token()
	token_info = spotify_oauth.refresh_access_token(token_info['refresh_token'])
	token = token_info['access_token']
	sp = spotipy.Spotify(auth=token)
	return sp
