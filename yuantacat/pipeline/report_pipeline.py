#-*- coding: utf-8 -*-

from yuantacat.pipeline.state.entry_list_helper import EntryListHelper
from yuantacat.report.capital_increase_history_data_creator import CapitalIncreaseHistoryDataCreator
from yuantacat.report.capital_structure_data_creator import CapitalStructureDataCreator
from yuantacat.report.cash_flow_data_creator import CashFlowDataCreator
from yuantacat.report.dividend_policy_data_creator import DividendPolicyDataCreator
from yuantacat.report.dupont_data_creator import DupontDataCreator
from yuantacat.report.liquidity_data_creator import LiquidityDataCreator
from yuantacat.report.operating_revenue_data_creator import OperatingRevenueDataCreator
from yuantacat.report.profitability_data_creator import ProfitabilityDataCreator
from yuantacat.report.revenue_index_data_creator import RevenueIndexDataCreator

import logging

class ReportPipeline():
    def __init__(self):
        self.logger = logging.getLogger(__name__)

        self.default_creator_list = [
            CapitalIncreaseHistoryDataCreator(),
            DividendPolicyDataCreator(),
            OperatingRevenueDataCreator(),
        ]
        self.period_creator_list = [
            CapitalStructureDataCreator(), 
            CashFlowDataCreator(),
            DupontDataCreator(),
            LiquidityDataCreator(),
            ProfitabilityDataCreator(),
            RevenueIndexDataCreator(),
        ]

    def run(self):
        stock_symbol_list = EntryListHelper().get_stock_symbol_list()
        for entry in stock_symbol_list:
            self.__run_stock_symbol(entry)

    def __run_stock_symbol(self, entry):
        self.logger.info('run report data creator list: {0}'.format(entry))

        param = self.__build_param(entry['stock_symbol'])

        creator_list = self.default_creator_list
        for creator in creator_list:
            creator.create(param['default'])

        creator_list = self.period_creator_list
        for creator in creator_list:
            creator.create(param['yearly'])
            creator.create(param['quarterly'])

    def __build_param(self, stock_symbol):
        return {
            'default' : { 
                'stock_symbol' : stock_symbol,
            }, 
            'yearly' : {
                'stock_symbol' : stock_symbol,
                'period' : 'Y', 
            },
            'quarterly' : {
                'stock_symbol' : stock_symbol,
                'period' : 'Q', 
            },
        }
