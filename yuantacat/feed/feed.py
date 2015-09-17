#-*- coding: utf-8 -*-

class Feed():
    def __init__(self, content):
        self.content = content

    def get(self):
        return self.content