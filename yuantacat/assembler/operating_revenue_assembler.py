#-*- coding: utf-8 -*-

from yuantacat.assembler.content_screener import ContentScreener
from yuantacat.common.string_utils import StringUtils
from yuantacat.common.lxml_utils import LxmlUtils
from yuantacat.dao.operating_revenue_dao import OperatingRevenueDao

import lxml.html

class OperatingRevenueAssembler():
    def __init__(self):
        self.base_xpath = '//html/body/div[@id="SysJustIFRAMEDIV"]/table/tr/td/form/table/tr/td/table'
        self.content_screener = ContentScreener()
        self.string_utils = StringUtils()
        self.lxml_utils = LxmlUtils()

    def assemble(self, param):
        content, stock_symbol = param['content'], param['stock_symbol']
        self.content_screener.screen(param)
        html_object = self.__get_html_object(content)
        relative_html_object = self.__traverse_to_relative_html_object(html_object)
        column_name_list = self.__assemble_column_name_list(relative_html_object)
        row_list = self.__assemble_row_list(relative_html_object)
        return OperatingRevenueDao(column_name_list, row_list, stock_symbol, 'M')

    def __get_html_object(self, content):
        content = self.string_utils.normalize_string(content)
        content = content.replace(u'<br>', u'')
        return lxml.html.fromstring(content)

    def __traverse_to_relative_html_object(self, html_object):
        relative_html_object_list = html_object.xpath(self.base_xpath)
        assert len(relative_html_object_list) > 0, 'invalid base_xpath (table_tags)'
                
        return relative_html_object_list[0]

    def __assemble_column_name_list(self, relative_html_object):
        # traverse and sanity check
        tr_tags = relative_html_object.xpath('./tr')
        assert len(tr_tags) > 5, 'invalid tr_tags'

        td_texts = tr_tags[5].xpath('./td/text()')
        assert len(td_texts) == 7, 'invalid td_texts size, should be 7'

        return [text.strip() for text in td_texts]

    def __assemble_row_list(self, relative_html_object):
        tr_tags = relative_html_object.xpath('./tr')
        assert len(tr_tags) > 5, 'invalid tr_tags'

        return [self.__assemble_row(tr_tag) for tr_tag in tr_tags[6:]]

    def __assemble_row(self, relative_html_object):
        td_tags = relative_html_object.xpath('./td')
        td_texts = self.lxml_utils.get_text_list(td_tags)
        assert len(td_texts) == 7, 'invalid td_texts size, should be 7'
        row = []

        # should be stmt_date
        stmt_date = self.string_utils.from_local_string_to_date(td_texts[0])
        row.append(stmt_date)

        # should be number 
        for number_string in td_texts[1:]:
            number = self.string_utils.normalize_number(number_string)
            row.append(number)

        return row
