import Speech
import Spotify
import Wiki

voice = Speech.Speech()
# track_player = Spotify.PlaySong()
wiki = Wiki.Wiki()

wiki_summary = wiki.getWikiSummary("Stack Overflow")

# input = voice.record_speech()
# artist, track = voice.parse_spotify_track(input)

# track_player.refresh_auth()
# track_player.play_song(artist, track)

language = "en"

voice.output_speech(text=wiki_summary, language=language)