#-*- coding: utf-8 -*-

from yuantacat.pipeline.pipeline import Pipeline
from yuantacat.spider.cash_flow_spider import CashFlowQuarterlySpider
from yuantacat.spider.cash_flow_spider import CashFlowYearlySpider
from yuantacat.assembler.cash_flow_assembler import CashFlowQuarterlyAssembler
from yuantacat.assembler.cash_flow_assembler import CashFlowYearlyAssembler
from yuantacat.feed.cash_flow_feed import CashFlowFeedBuilder

class CashFlowQuarterlyPipeline(Pipeline):
    def __init__(self):
        param = {
            'memento_path' : './yuantacat/data/memento/cash_flow_quarterly.json',
            'default_value_param' : 'stock_symbol',
            'spider' : CashFlowQuarterlySpider(), 
            'assembler' : CashFlowQuarterlyAssembler(), 
            'feed_builder' : CashFlowFeedBuilder(),
        }
        Pipeline.__init__(self, param)

class CashFlowYearlyPipeline(Pipeline):
    def __init__(self):
        param = {
            'memento_path' : './yuantacat/data/memento/cash_flow_yearly.json',
            'default_value_param' : 'stock_symbol',
            'spider' : CashFlowYearlySpider(), 
            'assembler' : CashFlowYearlyAssembler(), 
            'feed_builder' : CashFlowFeedBuilder(),
        }
        Pipeline.__init__(self, param)