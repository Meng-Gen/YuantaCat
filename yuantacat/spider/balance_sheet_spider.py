#-*- coding: utf-8 -*-

from yuantacat.spider.spider import Spider

class BalanceSheetSummarySpider(Spider):
    def build_url(self, param):
        return '''http://jdata.yuanta.com.tw/z/zc/zcp/zcp_%s.djhtm''' % (param['stock_symbol'])

    def build_key(self, param):
        return '''balance_sheet_summary/%s''' % (param['stock_symbol'])

class BalanceSheetQuarterlySpider(Spider):
    def build_url(self, param):
        return '''http://jdata.yuanta.com.tw/z/zc/zcp/zcpa/zcpa_%s.djhtm''' % (param['stock_symbol'])

    def build_key(self, param):
        return '''balance_sheet_quarterly/%s''' % (param['stock_symbol'])

class BalanceSheetYearlySpider(Spider):
    def build_url(self, param):
        return '''http://jdata.yuanta.com.tw/z/zc/zcp/zcpb/zcpb_%s.djhtm''' % (param['stock_symbol'])

    def build_key(self, param):
        return '''balance_sheet_yearly/%s''' % (param['stock_symbol'])
