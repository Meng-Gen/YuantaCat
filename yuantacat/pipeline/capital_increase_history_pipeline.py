#-*- coding: utf-8 -*-

from yuantacat.pipeline.state.state_machine import StateMachine
from yuantacat.pipeline.state.entry_list_helper import EntryListHelper
from yuantacat.spider.capital_increase_history_spider import CapitalIncreaseHistorySpider
from yuantacat.assembler.capital_increase_history_assembler import CapitalIncreaseHistoryAssembler
from yuantacat.feed.capital_increase_history_feed import CapitalIncreaseHistoryFeedBuilder

import datetime

class CapitalIncreaseHistoryPipeline(StateMachine):
    def __init__(self, memento_path='./yuantacat/data/memento/capital_increase_history.json'):
        memento_param = {
            'path' : memento_path, 
            'default_value' : self.__get_default_value(),
            'filter_key_list' : [ 'state', 'all_entry_list', 'todo_entry_list', 'last_updated_date' ],
        }
        transition_table = [
            ('InitialState', 'LoadState', ''),
            ('LoadState', 'SpiderState', 'spider'),
            ('LoadState', 'AssemblerState', 'assembler'),
            ('LoadState', 'AssemblerState', 'database'),
            ('LoadState', 'FinalState', 'final'),
            ('SpiderState', 'AssemblerState', ''), 
            ('AssemblerState', 'DatabaseState', ''), 
            ('DatabaseState', 'FinalState', ''), 
        ]
        param = {
            'memento' : memento_param,
            'transition_table' : transition_table,
            'spider' : CapitalIncreaseHistorySpider(), 
            'assembler' : CapitalIncreaseHistoryAssembler(), 
            'feed_builder' : CapitalIncreaseHistoryFeedBuilder(),
        }
        StateMachine.__init__(self, param)

    def __get_default_value(self):
        stock_symbol_list = EntryListHelper().get_stock_symbol_list()
        # !!! DEBUG ONLY !!!
        stock_symbol_list = stock_symbol_list[:1]
        return {
            'state' : 'spider',
            'all_entry_list' : list(stock_symbol_list),
            'todo_entry_list' : list(stock_symbol_list),
            'last_updated_date' : datetime.date(1949, 12, 7) 
        }
