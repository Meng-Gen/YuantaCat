#-*- coding: utf-8 -*-

from yuantacat.feed.feed import Feed
from yuantacat.feed.yuanta_feed_builder import YuantaFeedBuilder

class CapitalIncreaseHistoryFeed(Feed):
    pass

class CapitalIncreaseHistoryFeedBuilder():
    def build(self, dao):
        builder = YuantaFeedBuilder([u'現金增資', u'盈餘轉增資', u'公積及其他'], [1, 3, 5])
        tuple_feed = builder.build(dao)
        return CapitalIncreaseHistoryFeed(tuple_feed)
