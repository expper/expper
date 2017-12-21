import re
import os
import sqlite3
import wikipedia
import xml.etree.ElementTree as ET
import numpy as np
import cv2
from location import location
from classify_image import classify_image
#from object_recognition import capture


class config:
    def __init__(self, r): 
        self.root = r
        self.EMOTION = self.root.find('EMOTION')

    def get_EMOTION_state(self):
        return self.EMOTION.text

    def set_EMOTION_state(self, s):
        self.EMOTION.text = s

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

    def __detect_teg(self, l, ls, index, k):
        if k < len(l):
            tg = db_manager().get_tags_object().get_tags()
            t = ""
            r = ""
            for i in range(index, k + 1):
                _t1 = "" if i == k else "_"
                _t2 = "" if i == k else " "
                t += l[i] + _t1
                r += l[i] + _t2
            t = tg.get(t)
            if t != None:
                ls.append(t)
                self.current_question = self.current_question.replace(r, "")
                return True
        return False


    def get_taged_string(self, l):
        self.current_question = re.sub(r'[^\w]', ' ', self.current_question).lower()
        l = re.sub(r'[^\w]', ' ', l).lower().split(" ")
        tg = db_manager().get_tags_object().get_tags()
        index = 0
        ls = list()
        for i in range(0, len(l)):
            for j in range(len(l) - 1, i - 1, -1):
                k = self.__detect_teg(l, ls, i, j)
                if k == True:
                    break
        if len(ls) == 0:
            ls.append("None")
        return ls

    def __replace_attrs(self, t, f):
        for i in f:
            t = t.replace(i, f[i])
        return t

    def __is_unknown_attr(self, f):
        if len(f) == 0:
            return False
        for i in f:
            if f[i] == "":
                return True
        return False

    def __detected_object_to_answer(self, d):
        f = 0
        s = ""
        for i in d:
            if f < d[i]:
                f = d[i]
                s = i
        return s

    def __get_path_of_image(self):
        #ss = capture()
        #return ss.get_path()
        cap = cv2.VideoCapture(1)
        ret, frame = cap.read()
        cv2.imwrite("pt.png", frame)
        cap.release()
        cv2.destroyAllWindows()
        return "pt.png"

    def __wiki_full_search(self):
        s = wikipedia.page(self.current_questionr)
        s = re.sub(r'\(.+\)', ' ', s)
        s = re.sub(r'\".+\"', ' ', s)
        return s
    def __wiki_summary_search(self):
        s = wikipedia.summary(self.current_questionr)
        s = re.sub(r'\(.+\)', ' ', s)
        s = re.sub(r'\".+\"', ' ', s)
        return s
    def __wiki_search(self):
        s = wikipedia.summary(self.current_question, sentences=1)
        s = re.sub(r'\(.+\)', ' ', s)
        s = re.sub(r'\".+\"', ' ', s)
        return s

    def __get_attrs(self, r):
        l = r.attrib
        ll = {}
        for i in l:
            if i[0] == '_':
                try:
                    if l[i] == "_NAME_FROM_FACE":
                        ll[i] = "John" #get face image from camera and find in DB
                    elif l[i] == "_TEXT_FROM_OBJECT":
                        c_img = classify_image()
                        path = self.__get_path_of_image()
                        ll[i] = self.__detected_object_to_answer(c_img.detect_image(path))
                        os.remove(path)
                    elif l[i] == "_FIND_LOCATION":
                        loc = location()
                        ll[i] = str(loc.find_location_for(self.current_question))
                    elif l[i] == "_WIKI_SEARCH":
                        ll[i] = self.__wiki_search()
                    elif l[i] == "_WIKI_SUMMARY_SEARCH":
                        ll[i] = self.__wiki_summary_search()
                    elif l[i] == "_WIKI_FULL_SEARCH":
                        ll[i] = self.__wiki_full_search()
                    else:
                        ll[i] = ""
                except:
                    ll[i] = ""
        return ll 

    def __add_answer_if_exist(self, r):
        c = db_manager().get_config_object()
        b = False
        for i in r:
            m = i.get('EMOTION')
            if m == c.get_EMOTION_state() or m == "0":
                ff = self.__get_attrs(i)
                if self.__is_unknown_attr(ff):
                    continue
                for j in i:
                    if j.tag == "answer":
                        txt = self.__replace_attrs(j.text, ff)
                        self.answer += txt + " "
                        b = True
                    if j.tag == "EMOTION":
                        c.set_EMOTION_state(j.text)
                break
        return b


    def find_answer(self, r, index = 0):
        if index < len(self.question) and r.tag == self.question[index]:
            if True == self.__add_answer_if_exist(r):
                del self.question[0:index + 1]
            else:
                for i in r:
                    self.find_answer(i, index + 1)

    def get_answer(self, s):
        self.current_question = s
        self.question = self.get_taged_string(s)
        self.answer = ""
        for i in self.roots:
            self.find_answer(i)
            if len(self.question) == 0:
                break
        self.question = ""
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

    def find_phrases(self):
        c = db_manager().get_config_object()
        l = list()
        for i in self.root:
            m = i.get('EMOTION')
            if m == c.get_EMOTION_state() or m == "0":
                l.append(i.text)
        return l


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
