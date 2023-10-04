import Speech
import Spotify

voice = Speech.Speech()
# track_player = Spotify.PlaySong()

# input = voice.record_speech()
# artist, track = voice.parse_spotify_track(input)

# track_player.refresh_auth()
# track_player.play_song(artist, track)

text = "This is some test text"
language = "en"

voice.output_speech(text=text, language=language)