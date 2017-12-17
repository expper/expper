import os
import re

class text_to_voice:


    def to_voice(self, s):
        #s = re.sub(r'[^\w]', ' ', s)
        print("ANSWER--> ", s)
        os.system("google_speech -l en \"" + s + "\"")  







