import spotipy

from fastapi import APIRouter

from auth.spotify import get_sp, refresh_token


router = APIRouter()

SP = get_sp()


@router.get("/user_info/", tags=["user_info"])
async def read_users():
    global SP
    try:
        user = SP.me()
    except spotipy.exceptions.SpotifyException as e:
        SP = refresh_token()
        user = SP.me()
    res = {
        "username": user["id"],
        "userpic": user["images"][0]["url"],
        "country": user["country"]
    }
    print("*** fetch user's info")
    return res

