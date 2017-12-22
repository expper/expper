from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import datetime
#from time import sleep


class time_comparator:

    def __init__(self):
        self.update()
        #sleep(3)

    def update(self):
        self.current_time = datetime.datetime.now()

    def get_time_diff_S(self):
        n = datetime.datetime.now() - self.current_time
        return n.seconds

    def get_time_diff_M(self):
        return self.get_time_diff_S() / 60


