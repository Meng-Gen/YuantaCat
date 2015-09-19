#-*- coding: utf-8 -*-

from yuantacat.feed.feed import Feed
from yuantacat.feed.financial_feed_builder import FinancialFeedBuilder

class BalanceSheetFeed(Feed):
    pass 

class BalanceSheetFeedBuilder():
    def build(self, dao):
        tuple_feed = FinancialFeedBuilder().build(dao)
        return BalanceSheetFeed(tuple_feed)
