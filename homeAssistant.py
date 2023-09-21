import Speech
import Spotify

recorder = Speech.Speech()
track_player = Spotify.PlaySong()

input = recorder.record_speech()
artist, track = recorder.parse_spotify_track(input)

track_player.refresh_auth()
track_player.play_song(artist, track)