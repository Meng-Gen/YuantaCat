#-*- coding: utf-8 -*-

from yuantacat.spider.storage.spider_storage import SpiderStorage
from yuantacat.common.string_utils import StringUtils

class Spider():
    def __init__(self):
        self.storage = SpiderStorage()
        self.string_utils = StringUtils()
        
    def crawl(self, param):
        param = self.__extend_param(param)
        url = self.build_url(param)
        key = self.build_key(param)
        self.storage.set(key, url)

    def is_crawled(self, param):
        param = self.__extend_param(param)
        key = self.build_key(param)
        return self.storage.contains(key)

    def get_crawled(self, param):
        param = self.__extend_param(param)
        key = self.build_key(param)
        return self.storage.get(key)

    def __extend_param(self, param):
        output = {}
        if 'stock_symbol' in param:
            output['stock_symbol'] = param['stock_symbol']
        if 'market_type' in param:
            market_type = param['market_type']
            output['market_type'] = market_type
            output['market_mode'] = self.__extend_market_mode(market_type)
        return output

    def __extend_market_mode(self, market_type):
        mode_map = {
            'stock_exchange_market' : '2',
            'otc_market' : '4',
        }
        return mode_map[market_type]

    def build_url(self, param):
        raise NotImplementedError

    def build_key(self, param):
        raise NotImplementedError
