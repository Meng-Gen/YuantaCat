#-*- coding: utf-8 -*-

from yuantacat.pipeline.pipeline import Pipeline
from yuantacat.spider.dividend_policy_spider import DividendPolicySpider
from yuantacat.assembler.dividend_policy_assembler import DividendPolicyAssembler
from yuantacat.feed.dividend_policy_feed import DividendPolicyFeedBuilder

class DividendPolicyPipeline(Pipeline):
    def __init__(self):
        param = { 
            'memento_path' : './yuantacat/data/memento/dividend_policy.json',
            'default_value_param' : 'stock_symbol',
            'spider' : DividendPolicySpider(), 
            'assembler' : DividendPolicyAssembler(), 
            'feed_builder' : DividendPolicyFeedBuilder(),
        }
        Pipeline.__init__(self, param)
