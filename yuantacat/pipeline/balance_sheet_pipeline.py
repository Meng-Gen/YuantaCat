#-*- coding: utf-8 -*-

from yuantacat.pipeline.pipeline import Pipeline
from yuantacat.spider.balance_sheet_spider import BalanceSheetQuarterlySpider
from yuantacat.spider.balance_sheet_spider import BalanceSheetYearlySpider
from yuantacat.assembler.balance_sheet_assembler import BalanceSheetQuarterlyAssembler
from yuantacat.assembler.balance_sheet_assembler import BalanceSheetYearlyAssembler
from yuantacat.feed.balance_sheet_feed import BalanceSheetFeedBuilder

class BalanceSheetQuarterlyPipeline(Pipeline):
    def __init__(self):
        param = {
            'memento_path' : './yuantacat/data/memento/balance_sheet_quarterly.json',
            'default_value_param' : 'stock_symbol',
            'spider' : BalanceSheetQuarterlySpider(), 
            'assembler' : BalanceSheetQuarterlyAssembler(), 
            'feed_builder' : BalanceSheetFeedBuilder(),
        }
        Pipeline.__init__(self, param)

class BalanceSheetYearlyPipeline(Pipeline):
    def __init__(self):
        param = {
            'memento_path' : './yuantacat/data/memento/balance_sheet_yearly.json',
            'default_value_param' : 'stock_symbol',
            'spider' : BalanceSheetYearlySpider(), 
            'assembler' : BalanceSheetYearlyAssembler(), 
            'feed_builder' : BalanceSheetFeedBuilder(),
        }
        Pipeline.__init__(self, param)