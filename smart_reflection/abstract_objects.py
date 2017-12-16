from enum import Enum
from db_objects import *
from text_to_voice import text_to_voice


class object_type(Enum):
    ABSTRACT = 1
    INPUT = 2
    INPUT_VOICE = 3
    OUTPUT = 4
    OUTPUT_VOICE = 5

class abstract_object:

    def __init__(self, t):
        self._type = t

    def get_type():
        return self._type

class output_object(abstract_object):

    def __init__(self):
        super().__init__(object_type.OUTPUT)

    def __init__(self, t):
        super().__init__(t)

    def run(self):
        return

class output_voice(output_object):

    def __init__(self, t):
        super().__init__(object_type.OUTPUT_VOICE)
        self.__m_text = t
        self.__m_text_to_voice = text_to_voice()

    def run(self):
        self.__m_text_to_voice.to_voice(self.__m_text)


class input_object(abstract_object):

    def __init__(self):
        super().__init__(object_type.INPUT)

    def __init__(self, t):
        super().__init__(t)

    def to_output_object(self):
        return output_object()

class input_voice(input_object):

    def __init__(self, t):
        super().__init__(object_type.INPUT_VOICE)
        self.__m_text = t

    def get_text(self):
        return self.__m_text

    def to_output_object(self):
        sp = db_manager().get_speach_object()
        txt = sp.get_answer(self.__m_text)
        return output_voice(txt)
            
class input_phrase(input_object):

    def __init__(self, t):
        super().__init__(object_type.INPUT_VOICE)
        self.__m_text = t

    def get_text(self):
        return self.__m_text

    def to_output_object(self):
        return output_voice(self.__m_text)





