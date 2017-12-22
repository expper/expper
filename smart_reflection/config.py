from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import xml.etree.ElementTree as ET

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

