#-*- coding: utf-8 -*-

from yuantacat.spider.storage.file_spider_storage import FileSpiderStorage

class SpiderStorage():
    def __init__(self):
        self.impl = FileSpiderStorage()

    def set(self, key, url):
        self.impl.set(key, url)

    def contains(self, key):
        return self.impl.contains(key)

    def get(self, key):
        return self.impl.get(key)
