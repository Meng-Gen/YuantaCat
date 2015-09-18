#-*- coding: utf-8 -*-

from yuantacat.feed.feed import Feed
from yuantacat.feed.yuanta_feed_builder import YuantaFeedBuilder

class OperatingRevenueFeed(Feed):
    pass

class OperatingRevenueFeedBuilder():
    def build(self, dao):
        builder = YuantaFeedBuilder([u'合併營收'], [1])
        tuple_feed = builder.build(dao)
        return OperatingRevenueFeed(tuple_feed)
