from dotenv import load_dotenv
import os
from requests_oauthlib import OAuth2Session
from requests.auth import HTTPBasicAuth
import requests
import json

load_dotenv()

class Refresh:

    def __init__(self):
        self.refresh_token = os.getenv("SPOTIFY_REFRESH_TOKEN")
        self.base_64 = os.getenv("SPOTIFY_BASE_64")

    def refresh(self):
        query = "https://accounts.spotify.com/api/token"

        response = requests.post(query,
                                 data={"grant_type": "refresh_token",
                                       "refresh_token": os.getenv("SPOTIFY_REFRESH_TOKEN")},
                                 headers={"Authorization": "Basic " + os.getenv("SPOTIFY_BASE_64")})

        response_json = response.json()
        print(response_json)

        return response_json["access_token"]

a = Refresh()
a.refresh()

# # Credentials you get from registering a new application
# client_id = os.getenv("SPOTIFY_CLIENT_ID")
# client_secret = os.getenv("SPOTIFY_SECRET")
# redirect_uri = 'https://localhost:3000'
# # 
# # OAuth endpoints given in the Spotify API documentation
# # https://developer.spotify.com/documentation/general/guides/authorization/code-flow/
# authorization_base_url = "https://accounts.spotify.com/authorize"
# token_url = "https://accounts.spotify.com/api/token"
# # https://developer.spotify.com/documentation/general/guides/authorization/scopes/
# scope = [
#     "user-modify-playback-state",
#     "user-read-playback-state"
# ]
# # 
# # 
# spotify = OAuth2Session(client_id, scope=scope, redirect_uri=redirect_uri)
# # 
# # Redirect user to Spotify for authorization
# authorization_url, state = spotify.authorization_url(authorization_base_url)
# print('Please go here and authorize: ', authorization_url)
# # 
# # Get the authorization verifier code from the callback url
# redirect_response = input('\n\nPaste the full redirect URL here: ')
# # 
# # 
# # 
# auth = HTTPBasicAuth(client_id, client_secret)
# # 
# # Fetch the access token
# token = spotify.fetch_token(token_url, auth=auth, authorization_response=redirect_response)
# # 
# print(token)
# # 
# # Fetch a protected resource, i.e. user profile
# r = spotify.get('https://api.spotify.com/v1/me')
# print(r.content)