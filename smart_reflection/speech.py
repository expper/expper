from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import re
from location import location
from wiki import wiki
from object_recognition import object_recognition
from transaction import speech_transaction

class speech:
    def __init__(self, r, t, c):
        self.config = c
        self.tag = t
        self.roots = r
        self.answer = ""
        self.question = ""
        self.transacrion = speech_transaction()

    def __detect_teg(self, l, ls, index, k):
        if k < len(l):
            tg = self.tag.get_tags()
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
        tg = self.tag.get_tags()
        index = 0
        ls = list()
        for i in range(0, len(l)):
            for j in range(len(l) - 1, i - 1, -1):
                k = self.__detect_teg(l, ls, i, j)
                if k == True:
                    break
        for i in range(0, len(ls)):
            if ls[i] == "relate":
                d = self.transacrion.get_last_speech()
                if d != "":
                    ls[i] = ""
                    self.current_question = d

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

    def __get_attrs(self, r):
        l = r.attrib
        ll = {}
        for i in l:
            if i[0] == '_':
                try:
                    if l[i] == "_NAME_FROM_FACE":
                        ll[i] = "John" #get face image from camera and find in DB
                    elif l[i] == "_TEXT_FROM_OBJECT":
                        ll[i] = object_recognition().detect_image()
                    elif l[i] == "_FIND_LOCATION":
                        ll[i] = str(location().find_location_for(self.current_question))
                    elif l[i] == "_WIKI_SEARCH":
                        ll[i] = wiki().wiki_search(self.current_question)
                    elif l[i] == "_WIKI_SUMMARY_SEARCH":
                        ll[i] = wiki().wiki_summary_search(self.current_question)
                    elif l[i] == "_WIKI_FULL_SEARCH":
                        ll[i] = wiki().wiki_full_search(self.current_question)
                    else:
                        ll[i] = ""
                except:
                    print("Exception when try to process XML instruction as a python function call.")
                    ll[i] = ""
        return ll 

    def __add_answer_if_exist(self, r):
        b = False
        for i in r:
            m = i.get('EMOTION')
            if m == self.config.get_EMOTION_state() or m == "0":
                ff = self.__get_attrs(i)
                if self.__is_unknown_attr(ff):
                    continue
                for j in i:
                    if j.tag == "answer":
                        txt = self.__replace_attrs(j.text, ff)
                        self.answer += txt + " "
                        b = True
                    if j.tag == "EMOTION":
                        self.config.set_EMOTION_state(j.text)
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
        self.transacrion.update(self.current_question)
        return self.answer

