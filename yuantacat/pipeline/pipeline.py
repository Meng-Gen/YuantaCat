#-*- coding: utf-8 -*-

from yuantacat.pipeline.state.state_machine import StateMachine
from yuantacat.pipeline.state.entry_list_helper import EntryListHelper

import datetime

class Pipeline(StateMachine):
    def __init__(self, param):
        state_machine_param = {
            'memento' : {
                'path' : param['memento_path'], 
                'default_value' : self.get_default_value(param['default_value_param']),
                'filter_key_list' : [ 
                    'state', 
                    'all_entry_list', 
                    'todo_entry_list', 
                    'last_updated_date' 
                ],
            },
            'transition_table' : [
                ('InitialState', 'LoadState', ''),
                ('LoadState', 'SpiderState', 'spider'),
                ('LoadState', 'AssemblerState', 'assembler'),
                ('LoadState', 'AssemblerState', 'database'),
                ('LoadState', 'FinalState', 'final'),
                ('SpiderState', 'AssemblerState', ''), 
                ('AssemblerState', 'DatabaseState', ''), 
                ('DatabaseState', 'FinalState', ''), 
            ],
            'spider' : param['spider'], 
            'assembler' : param['assembler'], 
            'feed_builder' : param['feed_builder'],
        }
        StateMachine.__init__(self, state_machine_param)

    def get_default_value(self, default_value_param):
        if default_value_param == 'stock_symbol':
            return self.__get_stock_symbol_default_value()
        elif default_value_param == 'market_type':
            return self.__get_market_type_default_value()

    def __get_stock_symbol_default_value(self):
        stock_symbol_list = EntryListHelper().get_stock_symbol_list()
        return {
            'state' : 'spider',
            'all_entry_list' : list(stock_symbol_list),
            'todo_entry_list' : list(stock_symbol_list),
            'last_updated_date' : datetime.date(1949, 12, 7) 
        }

    def __get_market_type_default_value(self):
        entry_list = EntryListHelper().get_market_type_list()
        return {
            'state' : 'spider',
            'all_entry_list' : list(entry_list),
            'todo_entry_list' : list(entry_list),
            'last_updated_date' : datetime.date(1949, 12, 7) 
        }