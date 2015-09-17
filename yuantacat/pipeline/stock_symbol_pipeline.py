#-*- coding: utf-8 -*-

from yuantacat.pipeline.pipeline import Pipeline
from yuantacat.spider.stock_symbol_spider import StockSymbolSpider
from yuantacat.assembler.stock_symbol_assembler import StockSymbolAssembler
from yuantacat.feed.stock_symbol_feed import StockSymbolFeedBuilder

class StockSymbolPipeline(Pipeline):
    def __init__(self):
        param = { 
            'memento_path' : './yuantacat/data/memento/stock_symbol.json',
            'default_value_param' : 'market_type',
            'spider' : StockSymbolSpider(), 
            'assembler' : StockSymbolAssembler(), 
            'feed_builder' : StockSymbolFeedBuilder(),
        }
        Pipeline.__init__(self, param)
