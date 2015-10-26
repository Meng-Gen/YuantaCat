#-*- coding: utf-8 -*-

import random
import time

class State():
    def run(self):
        pass

    def set_up(self):
        pass

    def tear_down(self):
        pass

    def avoid_blocking(self, a=1, b=2):
        time.sleep(random.randint(a, b))
