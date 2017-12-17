import speech_recognition as sr
import pyaudio

class voic_detection:

    def get_current_text(self):
        return "tell about Italy"
        # Record Audio
        self.m_rec = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = self.m_rec.listen(source)
        # Speech recognition using Google Speech Recognition
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use m_rec.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of m_rec.recognize_google(audio)`
            return self.m_rec.recognize_google(audio)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            return ""
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            return ""
