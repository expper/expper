from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

class phrase:
    def __init__(self, r):
        self.root = r

    def get_learning_phrase(self, m):
        i = self.root.find("learning")
        c = i.get('EMOTION')
        if m == c or c == "0":
            return i.text

    def get_learning_answer_phrase(self, m):
        i = self.root.find("learning_answer")
        c = i.get('EMOTION')
        if m == c or c == "0":
            return i.text

    def find_phrases(self):
        c = db_manager().get_config_object()
        l = list()
        for i in self.root:
            m = i.get('EMOTION')
            if m == c.get_EMOTION_state() or m == "0":
                l.append(i.text)
        return l


