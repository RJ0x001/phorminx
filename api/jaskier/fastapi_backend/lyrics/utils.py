import math


TRASH_COMP = ('live', 'explicit', 'remaster', 'bonus track', 'single version')


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


def good_trash_lyrics(lyrics) -> bool:
    if len(lyrics) > 2000:
        return False
    return True


def get_time_fot_next_track(progress, full_duration):
    return math.ceil((full_duration - progress) / 1000)


def no_song_response(next_request_sec=None):
    return {
        'song_error': {
            "info": "Can't get the current playing song on Spotify",
            "adv_check": True
        },
        'next_track': next_request_sec,
    }


def no_connection_exception():
    return {
        'song_error': {
            "info": "Failed to establish a connection with Spotify",
            "adv_check": False
        },
    }