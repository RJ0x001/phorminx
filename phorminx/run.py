import spotipy
import requests
import math
import time

from bs4 import BeautifulSoup

from utils.token import get_spotipy_token
from config.config import scope


def create_playlist_for_user(spotify_obj, spotify_username, playlist_name):
    """
    Create new Spotify playlist.
    """
    playlist = spotify_obj.user_playlist_create(spotify_username, playlist_name)
    return playlist['id']


def add_tracks_to_playlist(spotify_obj, spotify_username, playlist_id, tracks_ids,
                           tracks_per_requests=100):
    """
    adding Spotify tracks id to playlist
    """
    results = []
    for tracks_chunk in [tracks_ids[i:i + tracks_per_requests] for i in
                         range(0, len(tracks_ids), tracks_per_requests)]:
        results.append(spotify_obj.user_playlist_add_tracks(spotify_username,
                                                            playlist_id,
                                                            tracks_chunk))
    return results


def get_tracks_ids(spotipy_obj, tracks_list):
    """
    make list with Spotify id of the songs.
    find first title from Spotify search that match with last.fm track
    """
    tracks_id = []
    for track in tracks_list:
        full_track = track[0] + ' ' + track[1]
        song = spotipy_obj.search(full_track)['tracks']['items']
        for item in song:
            if item['artists'][0]['name'] == track[0]:
                tracks_id.append(item['id'])
                break
    return tracks_id


def get_loved_tracks(user: str) -> list:
    """
    Get list of loved tracks withs artist for last.fm user
    :param user: username
    :return: list (artist track)
    """
    res_list = []
    last_fm = requests.get('https://www.last.fm/user/%s/loved' % user)

    soup = BeautifulSoup(last_fm.content, "html.parser")
    c = int(soup.find('h1', 'content-top-header').text.replace('\n', '').replace(' ', '').split('(')[1][:-1])
    page_count = math.ceil(c / 50)
    for x in range(1, page_count + 1):
        if x == 1:
            for i in range(50):
                get_content(i, res_list, soup)
        else:
            last_fm = requests.get('https://www.last.fm/user/%s/loved?page=%s' % (user, x))
            for i in range(50):
                soup = BeautifulSoup(last_fm.content, "html.parser")
                get_content(i, res_list, soup)
    return res_list


def get_content(i: int, res_list: list, soup) -> None:
    """
    parse last.fm row with song
    """
    try:
        artist = soup.find_all('td', 'chartlist-artist')[i].findAll('a')[0].get('title')
        song = soup.find_all('td', 'chartlist-name')[i].findAll('a')[0].get('title')
        res_list.append((artist, song))
    except IndexError:
        pass


def run(lastfm_user):
    """
    Run the app
    """
    username, token = get_spotipy_token(scope)
    spotipy_object = spotipy.Spotify(auth=token)
    songs = get_loved_tracks(lastfm_user)
    tracks = get_tracks_ids(spotipy_object, songs)
    playlist_id = create_playlist_for_user(spotipy_object, username, 'fav tracks last.fm user %s' % lastfm_user)
    add_tracks_to_playlist(spotipy_object, username, playlist_id, tracks)
