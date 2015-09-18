#-*- coding: utf-8 -*-

from yuantacat.spider.spider import Spider

class ProfitabilitySpider(Spider):
    def build_url(self, param):
        return '''http://jdata.yuanta.com.tw/z/zc/zce/zce_%s.djhtm''' % (param['stock_symbol'])

    def build_key(self, param):
        return '''profitability/%s''' % (param['stock_symbol'])