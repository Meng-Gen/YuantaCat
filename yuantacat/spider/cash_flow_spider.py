#-*- coding: utf-8 -*-

from yuantacat.spider.spider import Spider

class CashFlowQuarterlySpider(Spider):
    def build_url(self, param):
        return '''http://jdata.yuanta.com.tw/z/zc/zc3/zc3_%s.djhtm''' % (param['stock_symbol'])

    def build_key(self, param):
        return '''cash_flow_quarterly/%s''' % (param['stock_symbol'])

class CashFlowYearlySpider(Spider):
    def build_url(self, param):
        return '''http://jdata.yuanta.com.tw/z/zc/zc3/zc3a_%s.djhtm''' % (param['stock_symbol'])

    def build_key(self, param):
        return '''cash_flow_yearly/%s''' % (param['stock_symbol'])
