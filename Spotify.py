import os
import requests

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

        return response_json["access_token"]

class PlaySong:

    def __init__(self):
        self.user_id = os.getenv("SPOTIFY_USER_ID")
        self.spotify_token = ""

    def play_song(self, artist, trackTitle):

        print(f"Attempting to play {trackTitle} by {artist}")

        search_headers = {
            'Authorization': 'Bearer {}'.format(self.spotify_token),
        }

        search_params = {
            'q': f'track:{trackTitle} artist:{artist}',
            'type': 'track',
            'limit': '1',
        }

        search_response = requests.get('https://api.spotify.com/v1/search', params=search_params, headers=search_headers)

        response_json = search_response.json()

        track_uri = response_json["tracks"]["items"][0]["uri"]

        self.play_track(track_uri)

    def play_track(self, uri):

        play_headers = {
            'Authorization': 'Bearer {}'.format(self.spotify_token),
            'Content-Type': 'application/json',
        }

        play_params = {
            'device_id': os.getenv("SPOTIFY_DEVICE_ID"),
        }

        play_json_data = {
            'uris': [
                uri,
            ],
            'position_ms': 0,
        }

        requests.put('https://api.spotify.com/v1/me/player/play', params=play_params, headers=play_headers, json=play_json_data)

    def refresh_auth(self):
        
        refreshObject = Refresh()
        self.spotify_token = refreshObject.refresh()