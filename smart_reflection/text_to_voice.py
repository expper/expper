import pyttsx

class text_to_voice:

    def __init__(self):
        self.__m_engine = pyttsx.init()

    def to_voice(self, s):
        #self.__m_engine.say(s)
        #self.__m_engine.runAndWait()
        print("ANSWER--> ", s)







