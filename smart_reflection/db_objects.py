from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sqlite3
from config import config
from speech import speech
from tags import tags
from phrase import phrase

import xml.etree.ElementTree as ET


class Singleton(type):
    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance

class db_manager(metaclass=Singleton):

    def __init__(self, p):
        self.connection = sqlite3.connect(p)
        self.cursor = self.connection.cursor()
        self.config = self.__get_config_object_from_db()
        self.tags   = self.__get_tags_object_from_db()
        self.phrase = self.__get_phrase_object_from_db()

        self.speech = self.__get_speech_object_from_db()
        
    def __del__(self):
        self.connection.close()

    def __get_xml(self, s):
        r = list()
        for i in self.cursor.execute("SELECT * FROM " + s ):
                r.append(ET.fromstring(i[1]))
        return r

    def __get_config_object_from_db(self):
        r = self.__get_xml('config')
        return config(r[0])

    def __get_speech_object_from_db(self):
        r = self.__get_xml('speech')
        return speech(r, self.tags, self.config, self.phrase, self)
        
    def __get_tags_object_from_db(self):
        r = self.__get_xml('tags')
        return tags(r[0])

    def __get_phrase_object_from_db(self):
        r = self.__get_xml('phrase')
        return phrase(r[0])

    def get_config_object(self):
        return self.config

    def get_speech_object(self):
        return self.speech

    def get_tags_object(self):
        return self.tags

    def get_phrase_object(self):
        return self.phrase

    def save_speech_learning(self, l):
        self.cursor.execute("DELETE FROM speech WHERE Tag = 'learning'")
        x = ET.tostring(l, encoding='utf8', method='xml').decode(encoding='utf8').replace('\'', '\"')
        print(x)
        self.cursor.execute("INSERT INTO speech VALUES ('" + l.tag + "', '" + x + "')")
        self.connection.commit()

