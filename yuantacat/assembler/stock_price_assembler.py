#-*- coding: utf-8 -*-

from yuantacat.common.string_utils import StringUtils
from yuantacat.dao.stock_price_dao import StockPriceDao

class StockPriceAssembler():
    def __init__(self):
        self.string_utils = StringUtils()

    def assemble(self, param):
        content, stock_symbol = param['content'], param['stock_symbol']
        lines = content.splitlines()
        column_name_list = self.__assemble_column_name_list(lines)
        row_list = self.__assemble_row_list(lines)
        return StockPriceDao(column_name_list, row_list, stock_symbol, 'D')

    def __assemble_column_name_list(self, lines):
        return lines[0].split(',')

    def __assemble_row_list(self, lines):
        return [self.__assemble_row(line) for line in lines[1:]]

    def __assemble_row(self, line):
        texts = line.split(',')

        row = []
        stmt_date = self.string_utils.from_local_string_to_date(texts[0])
        row.append(stmt_date)
        for number_string in texts[1:]:
            number = self.string_utils.normalize_number(number_string)
            row.append(number)
        return row
