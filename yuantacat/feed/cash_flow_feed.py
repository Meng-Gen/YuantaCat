#-*- coding: utf-8 -*-

from yuantacat.feed.feed import Feed
from yuantacat.feed.financial_feed_builder import FinancialFeedBuilder

class CashFlowFeed(Feed):
    pass 

class CashFlowFeedBuilder():
    def build(self, dao):
        tuple_feed = FinancialFeedBuilder().build(dao)
        return CashFlowFeed(tuple_feed)
