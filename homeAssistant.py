import Speech
import Spotify
import Wiki

voice = Speech.Speech()
track_player = Spotify.PlaySong()
wiki = Wiki.Wiki()

language = "en"

WAKE_PHRASE = "awaken"

print("Starting Etna...")

while True:
    print("Listening")
    input = voice.record_speech()

    if WAKE_PHRASE in input:
        voice.output_speech("I am ready", language)
        input = voice.record_speech()

        if "play" in input:
            artist, track = voice.parse_spotify_track(input)

            track_player.refresh_auth()
            track_player.play_song(artist, track)
        elif "search" in input:
            wiki_title = voice.parse_from(input, "search ")
            wiki_summary = wiki.getWikiSummary(wiki_title)
            
            voice.output_speech(wiki_summary, language)
        else:
            voice.output_speech("Command not recognised", language)