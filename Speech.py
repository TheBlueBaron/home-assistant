from gtts import gTTS
from playsound import playsound

import speech_recognition as sr

class Speech():

    def output_speech(self, text, language):

        speech = gTTS(text=text, lang=language, slow=False)

        speech.save("outSpeech.mp3")

        playsound("outSpeech.mp3")

    def record_speech(self):

        r = sr.Recognizer()
        with sr.Microphone() as source:
            speech = r.listen(source)
            input = ""

            try:
                input = r.recognize_google(speech)
                print(input)
            except Exception as e:
                print("Exception: " + str(e))

        return input.lower()

    def parse_between(self, input, first, last):
        
        start = input.index( first ) + len( first )
        end = input.index( last, start )
        parsed_input = input[start:end]

        return parsed_input

    def parse_from(self, input, delim):

        return input.partition(delim)[2]

    def parse_spotify_track(self, input):

        first = "play "
        last = " by"
        delim = "by "

        artist = self.parse_from(input, delim)
        track = self.parse_between(input, first, last)

        return artist, track


        

