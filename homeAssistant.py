import Speech
import Spotify
import Wiki
import Weather
import News

voice = Speech.Speech()
track_player = Spotify.PlaySong()
wiki = Wiki.Wiki()
weather = Weather.Weather()
news = News.News()

weather_locations = weather.get_weather_locations()
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
            wiki_summary = wiki.get_wiki_summary(wiki_title)
            
            voice.output_speech(wiki_summary, language)
        elif "weather" in input:
            weather_search_location = voice.parse_from(input, "weather ").title()
            site_id = weather.get_site_id(weather_locations, weather_search_location)
            forecast = weather.get_forecast(site_id)
            voice.output_speech(forecast, language)
        elif "news" in input:
            headlines = news.get_headlines()

            for headline in headlines:
                voice.output_speech(headline, "en")
        else:
            voice.output_speech("Command not recognised", language)