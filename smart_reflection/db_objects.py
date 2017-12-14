import re
import sqlite3
import xml.etree.ElementTree as ET


class config:
    def __init__(self, r): 
        self.root = r
        self.mood = self.root.find('mood')

    def get_mood_state(self):
        return self.mood.text

    def set_mood_state(self, s):
        self.mood.text = s

    def get_state(self, k):
        return self.root.find(k).text

    def set_state(self, k, v):
        s = self.root.find(k)
        if s != None:
            s.text = v

class speach:
    def __init__(self, r):
        self.roots = r
        self.answer = ""
        self.question = ""

    def get_taged_string(self, l):
        l = re.sub(r'[^\w]', ' ', l).lower().split(" ")
        tg = db_manager().get_tags_object().get_tags()
        index = 0
        ls = list()
        for i in l:
            t = tg.get(i)
            if t != None:
                ls.append(t)
            elif index + 1 < len(l):
                t = tg.get(l[index] + "_" + l[index + 1])
                if t != None:
                    ls.append(t)
                elif index + 2 < len(l):
                    t = tg.get(l[index] + "_" + l[index + 1] + "_" + l[index + 2])
                    if t != None:
                        ls.append(t)
            index += 1
        if len(ls) == 0:
            ls.append("None")
        return ls

#   def get_answer_(self, r, index = 0):
#       for i in r:
#           if i.tag == self.question[index]:
#               print(i.tag)
#
#   def exist_tag(self, r, s):
#       for i in r:
#           if s == i.tag:
#               return 1
#       return 0

    def get_answer(self, s):
        c = db_manager().get_config_object()
        self.question = self.get_taged_string(s)
        print(self.question)
#       self.answer = ""
#       for i in self.roots:
#           self.get_answer_(i)
#       self.question = ""
        return self.answer

class tags:
    def __init__(self, r):
        self.word_to_tag = dict()
        self.root = r
        for i in self.root:
            self.word_to_tag[i.tag] = i.text

    def get_tags(self):
        return self.word_to_tag;

class phrase:
    def __init__(self, r):
        self.root = r


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
        self.speach = self.__get_speach_object_from_db()
        self.config = self.__get_config_object_from_db()
        self.tags   = self.__get_tags_object_from_db()
        self.phrase = self.__get_phrase_object_from_db()
        
    def __del__(self):
        self.connection.close()

    def __get_xml(self, s):
        r = list()
        for i in self.cursor.execute("SELECT * FROM " + s ):
                r.append(ET.fromstring(i[0]))
        return r

    def __get_config_object_from_db(self):
        r = self.__get_xml('config')
        return config(r[0])

    def __get_speach_object_from_db(self):
        r = self.__get_xml('speach')
        return speach(r)
        
    def __get_tags_object_from_db(self):
        r = self.__get_xml('tags')
        return tags(r[0])

    def __get_phrase_object_from_db(self):
        r = self.__get_xml('phrase')
        return phrase(r[0])

    def get_config_object(self):
        return self.config

    def get_speach_object(self):
        return self.speach

    def get_tags_object(self):
        return self.tags

    def get_phrase_object(self):
        return self.phrase
