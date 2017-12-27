import os
import re

#import json
#from os.path import join, dirname
#from watson_developer_cloud import TextToSpeechV1
#import pygame


class text_to_voice:

   #def __init__(self):
   #    self.text_to_speech = TextToSpeechV1(
   #    username='ad9a4744-8815-4841-aa88-7ec7e891308c',
   #    password='Z4jjmvi8lKx8',
   #    x_watson_learning_opt_out=True)  # Optional flag

    def to_voice(self, text):
        #print("ANSWER--> ", text)
        os.system("/usr/local/bin/google_speech -l en \"" + text + "\"") 
   #    with open(join(dirname(__file__), './output.mp3'), 'wb') as audio_file:
   #        audio_file.write(self.text_to_speech.synthesize(text, accept='audio/mp3', voice="en-US_LisaVoice"))
   #        audio_file.close()
   #    pygame.mixer.init()
   #    pygame.mixer.music.load("output.mp3")
   #    os.remove("output.mp3")
   #    pygame.mixer.music.play()
   #    while pygame.mixer.music.get_busy() == True:
   #        continue







