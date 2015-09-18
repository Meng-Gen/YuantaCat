#-*- coding: utf-8 -*-

from yuantacat.spider.spider import Spider

class OperatingRevenueSpider(Spider):
    def build_url(self, param):
        return '''http://jdata.yuanta.com.tw/z/zc/zch/zch_%s.djhtm''' % (param['stock_symbol'])

    def build_key(self, param):
        return '''operating_revenue/%s''' % (param['stock_symbol'])