#-*- coding: utf-8 -*-

from yuantacat.pipeline.pipeline import Pipeline
from yuantacat.spider.capital_increase_history_spider import CapitalIncreaseHistorySpider
from yuantacat.assembler.capital_increase_history_assembler import CapitalIncreaseHistoryAssembler
from yuantacat.feed.capital_increase_history_feed import CapitalIncreaseHistoryFeedBuilder

class CapitalIncreaseHistoryPipeline(Pipeline):
    def __init__(self):
        param = {
            'memento_path' : './yuantacat/data/memento/capital_increase_history.json',
            'default_value_param' : 'stock_symbol',
            'spider' : CapitalIncreaseHistorySpider(), 
            'assembler' : CapitalIncreaseHistoryAssembler(), 
            'feed_builder' : CapitalIncreaseHistoryFeedBuilder(),
        }
        Pipeline.__init__(self, param)
