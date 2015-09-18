#-*- coding: utf-8 -*-

from yuantacat.pipeline.pipeline import Pipeline
from yuantacat.spider.profitability_spider import ProfitabilitySpider
from yuantacat.assembler.profitability_assembler import ProfitabilityAssembler
from yuantacat.feed.profitability_feed import ProfitabilityFeedBuilder

class ProfitabilityPipeline(Pipeline):
    def __init__(self):
        param = {
            'memento_path' : './yuantacat/data/memento/profitability.json',
            'default_value_param' : 'stock_symbol',
            'spider' : ProfitabilitySpider(), 
            'assembler' : ProfitabilityAssembler(), 
            'feed_builder' : ProfitabilityFeedBuilder(),
        }
        Pipeline.__init__(self, param)
