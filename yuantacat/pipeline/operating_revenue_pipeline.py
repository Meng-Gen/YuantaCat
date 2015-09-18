#-*- coding: utf-8 -*-

from yuantacat.pipeline.pipeline import Pipeline
from yuantacat.spider.operating_revenue_spider import OperatingRevenueSpider
from yuantacat.assembler.operating_revenue_assembler import OperatingRevenueAssembler
from yuantacat.feed.operating_revenue_feed import OperatingRevenueFeedBuilder

class OperatingRevenuePipeline(Pipeline):
    def __init__(self):
        param = {
            'memento_path' : './yuantacat/data/memento/operating_revenue.json',
            'default_value_param' : 'stock_symbol',
            'spider' : OperatingRevenueSpider(), 
            'assembler' : OperatingRevenueAssembler(), 
            'feed_builder' : OperatingRevenueFeedBuilder(),
        }
        Pipeline.__init__(self, param)
