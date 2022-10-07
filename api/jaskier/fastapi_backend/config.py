import os
from dotenv import load_dotenv

load_dotenv('../../../.env')

# Supported database types by name
MONGO_DB = "mongodb"

# Supported authentication providers by name
GOOGLE = "google-oidc"
SPOTIFY = "spotify-oidc"

# Selected database type to use
DATABASE_TYPE = MONGO_DB

# Front end endpoint
FRONTEND_URL = "http://localhost:3000"

# MongoDB Replica Set
MONGODB_HOST = os.environ.get("MONGODB_HOST", "127.0.0.1")
MONGODB_PORT = int(os.environ.get("MONGODB_PORT", 27017))
MONGODB_COLLECTION = "testdb"
MONGODB_DATABASE = "testdb"

# Google login
GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID", None)
GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET", None)
GOOGLE_DISCOVERY_URL = "https://accounts.google.com/.well-known/openid-configuration"
GOOGLE_REDIRECT_URL = "http://localhost:8000/google-login-callback/"


# SPOTIFY Client info
SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
SPOTIFY_AUTH_URL = 'https://accounts.spotify.com/authorize'
# SPOTIFY_REDIRECT_URI = os.getenv('SPOTIFY_REDIRECT_URI')
SPOTIFY_REDIRECT_URI = "http://localhost:8000/spotify-login-callback/"
SPOTIFY_TOKEN_URL = 'https://accounts.spotify.com/api/token'
SPOTIFY_ME_URL = 'https://api.spotify.com/v1/me'
SPOTIFY_SCOPE = 'user-read-currently-playing'


# GENIUS LYRICS
GENIUS_TOKEN = 'oq18Ynk0MDUqUO2PGKXqTxLH82-7ji9diIvTu-FpRmX7fNvMeFo5klHMnohURYUb'