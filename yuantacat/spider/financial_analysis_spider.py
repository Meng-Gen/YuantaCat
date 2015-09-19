#-*- coding: utf-8 -*-

from yuantacat.spider.spider import Spider

class FinancialAnalysisQuarterlySpider(Spider):
    def build_url(self, param):
        return '''http://jdata.yuanta.com.tw/z/zc/zcr/zcr_%s.djhtm''' % (param['stock_symbol'])

    def build_key(self, param):
        return '''financial_analysis_quarterly/%s''' % (param['stock_symbol'])

class FinancialAnalysisYearlySpider(Spider):
    def build_url(self, param):
        return '''http://jdata.yuanta.com.tw/z/zc/zcr/zcra_%s.djhtm''' % (param['stock_symbol'])

    def build_key(self, param):
        return '''financial_analysis_yearly/%s''' % (param['stock_symbol'])
