from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

class tags:
    def __init__(self, r):
        self.word_to_tag = dict()
        self.root = r
        for i in self.root:
            self.word_to_tag[i.tag] = i.text

    def get_tags(self):
        return self.word_to_tag;

