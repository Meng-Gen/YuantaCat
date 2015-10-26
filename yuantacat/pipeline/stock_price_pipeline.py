#-*- coding: utf-8 -*-

from yuantacat.pipeline.pipeline import Pipeline
from yuantacat.spider.stock_price_spider import StockPriceSpider
from yuantacat.assembler.stock_price_assembler import StockPriceAssembler
from yuantacat.feed.stock_price_feed import StockPriceFeedBuilder

class StockPricePipeline(Pipeline):
    def __init__(self):
        param = { 
            'memento_path' : './yuantacat/data/memento/stock_price.json',
            'default_value_param' : 'stock_symbol',
            'spider' : StockPriceSpider(), 
            'assembler' : StockPriceAssembler(), 
            'feed_builder' : StockPriceFeedBuilder(),
        }
        Pipeline.__init__(self, param)
