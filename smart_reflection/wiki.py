from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import re
import wikipedia

class wiki():
    def wiki_full_search(self, q):
        s = wikipedia.page(q)
        s = re.sub(r'\(.+\)', ' ', s)
        s = re.sub(r'\".+\"', ' ', s)
        return s
    def wiki_summary_search(self, q):
        s = wikipedia.summary(q)
        s = re.sub(r'\(.+\)', ' ', s)
        s = re.sub(r'\".+\"', ' ', s)
        return s
    def wiki_search(self, q):
        s = wikipedia.summary(q, sentences=1)
        if len(s) < 30:
            s = wikipedia.summary(q, sentences=2)
            if len(s) < 45:
                s = wikipedia.summary(q, sentences=3)
        s = re.sub(r'\(.+\)', ' ', s)
        s = re.sub(r'\".+\"', ' ', s)
        return s
