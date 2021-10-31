from flask_restful import Resource
from jaskier.functions import run_lyrics_search


class LyricsApiHandler(Resource):
    def get(self):
        res = run_lyrics_search()
        return {
            'resultStatus': 'SUCCESS',
            'artist': res["artist"],
            'song': res["song"],
            'lyrics': res["lyrics"],
            'artist_img': res['artist_img'],
            'album_title': res['album_title'],
            'timeLeft': res["next_track"],
        }
