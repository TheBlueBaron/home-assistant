from gtts import gTTS
from playsound import playsound

import speech_recognition as sr
import pyaudio
import wave

class Speech():

    def output_speech(self, text, language):

        speech = gTTS(text=text, lang=language, slow=False)

        speech.save("outSpeech.mp3")

        playsound("outSpeech.mp3")

    def record_speech(self):

        chunk = 1024
        sample_format = pyaudio.paInt16
        channels = 2
        fs = 44100
        seconds = 7
        filename = "test.wav"

        pa = pyaudio.PyAudio()

        print('Recording')

        stream = pa.open(format=sample_format, channels=channels, rate=fs, frames_per_buffer=chunk, input=True)

        frames = []

        for i in range(0, int(fs / chunk * seconds)):
            data = stream.read(chunk)
            frames.append(data)

        stream.stop_stream()
        stream.close()
        pa.terminate()

        print('Finished Recording')

        wf = wave.open(filename, 'wb')
        wf.setnchannels(channels)
        wf.setsampwidth(pa.get_sample_size(sample_format))
        wf.setframerate(fs)
        wf.writeframes(b''.join(frames))
        wf.close()

        r = sr.Recognizer()

        with sr.AudioFile(filename) as source:
            audio_data = r.record(source)
            text = r.recognize_google(audio_data)
            print('Recorded Speech:' + text)

        return text.lower()

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


        

