import sys
import random
from classify_image import classify_image
from enum import Enum
from db_objects import *
from helper_objects import time_comparator
from abstract_objects import *
from voic_detection import voic_detection

class base_state(Enum):
    UNKNOWN = 0
    STARTING = 1
    RUNNING = 2
    FINISHING = 3

class Singleton(type):
    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance

class controller(metaclass=Singleton):

    def __init__(self, p):
        print(':Starting:')
        self.__classify_img = classify_image()
        #print(self.__classify_img.detect_image('img'))
        self.time_cmp = time_comparator()
        self.db_manager = db_manager(db_name)
        self.__current_state = base_state.STARTING
        self.__m_voic_detection = voic_detection()
        self.__run()

    def __del__(self):
        print(':Finishing:')

    def __set_current_state(self, s):
        self.__current_state = s
        
    def get_current_state(self):
        return self.__current_state

    def get_input_objects(self):
        l = list();
        s = self.__m_voic_detection.get_current_text()
        if s != "":
            print("Question--> ", s)
            l.append(input_voice(s))
        elif self.time_cmp.get_time_diff_M() > 5:
            p = self.db_manager.get_phrase_object()
            ll = p.find_phrases()
            if len(ll) > 0:
                idx = random.randint(0, len(ll) - 1)
                l.append(input_phrase(ll[idx]))
        return l

    def to_outputs(self, l):
        s = list()
        for i in l:
            s.append(i.to_output_object())
        return s

    def process_outputs(self, l):
        for i in l:
            i.run()

    def __run(self):
        print(':Running:')
        self.__set_current_state(base_state.RUNNING)
        #while True:
        l = self.get_input_objects();
        if len(l) != 0:
            l = self.to_outputs(l)
            self.process_outputs(l)
            self.time_cmp.update()



if __name__ == "__main__":
    db_name = sys.argv[1]
    #try:
    controller(db_name)
    #except:



