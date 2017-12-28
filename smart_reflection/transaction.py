from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from helper_objects import time_


class Singleton(type):
    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance

class speech_transaction(metaclass=Singleton):

    def __init__(self):
        self.current_time = time_()
        self.last_speech = ""
        self.learning = False
        
    def update(self, s, b = False):
        self.learning = b
        self.current_time = time_()
        self.last_speech = s

    def is_learning(self):
        return self.learning

    def in_transaction(self):
        t = time_()
        if self.learning == True and abs(t.get_time_diff_S() - self.current_time.get_time_diff_S()) < 12:
            return True
        if abs(t.get_time_diff_S() - self.current_time.get_time_diff_S()) < 7:
            return True
        return False

    def get_last_speech(self):
        t = time_()
        if self.last_speech == "":
            self.learning = False
            return ""
        if self.learning == True and abs(t.get_time_diff_S() - self.current_time.get_time_diff_S()) < 12:
            self.current_time = time_()
            return self.last_speech
        if abs(t.get_time_diff_S() - self.current_time.get_time_diff_S()) > 5:
            self.learning = False
            self.last_speech = ""
            return ""
        self.current_time = time_()
        return self.last_speech





