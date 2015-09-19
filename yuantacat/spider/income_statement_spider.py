#-*- coding: utf-8 -*-

from yuantacat.spider.spider import Spider

class IncomeStatementQuarterlySpider(Spider):
    def build_url(self, param):
        return '''http://jdata.yuanta.com.tw/z/zc/zcq/zcq_%s.djhtm''' % (param['stock_symbol'])

    def build_key(self, param):
        return '''income_statement_quarterly/%s''' % (param['stock_symbol'])

class IncomeStatementYearlySpider(Spider):
    def build_url(self, param):
        return '''http://jdata.yuanta.com.tw/z/zc/zcq/zcqa_%s.djhtm''' % (param['stock_symbol'])

    def build_key(self, param):
        return '''income_statement_yearly/%s''' % (param['stock_symbol'])
