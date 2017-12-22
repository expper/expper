from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

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


