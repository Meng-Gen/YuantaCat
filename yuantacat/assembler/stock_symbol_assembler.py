#-*- coding: utf-8 -*-

from yuantacat.common.string_utils import StringUtils
from yuantacat.dao.stock_symbol_dao import StockSymbolDao

import lxml.html

class StockSymbolAssembler():
    def __init__(self):
        self.base_xpath = '//html/body'
        self.string_utils = StringUtils()

    def assemble(self, param):
        content = self.string_utils.normalize_string(param['content'])
        html_object = lxml.html.fromstring(content)
        relative_html_object = self.__traverse_to_relative_html_object(html_object)
        release_date = self.__assemble_release_date(relative_html_object)
        column_name_list = self.__assemble_column_name_list(relative_html_object)
        row_list = self.__assemble_row_list(relative_html_object)
        return StockSymbolDao(column_name_list, row_list, release_date)

    def __traverse_to_relative_html_object(self, html_object):
        relative_html_object_list = html_object.xpath(self.base_xpath)
        assert len(relative_html_object_list) == 1, 'invalid base_xpath'
        return relative_html_object_list[0]

    def __assemble_release_date(self, relative_html_object):
        # try to get release date
        table_tags = relative_html_object.xpath('./table')
        assert len(table_tags) > 0, 'invalid table_tags'

        headline_tags = table_tags[0].xpath('./h2')
        assert len(headline_tags) > 0, 'invalid headline_tags'
        
        headline_texts = headline_tags[1].xpath('./strong/center')
        groups = self.string_utils.match(u'^最近更新日期:(.*)$', headline_texts[0].text.strip())
        assert len(groups) > 0, 'could not match ^最近更新日期:(.*)$'
        
        release_date = self.string_utils.from_local_string_to_date(groups[0])
        return release_date

    def __assemble_column_name_list(self, relative_html_object):
        # traverse and sanity check
        tr_tags = relative_html_object.xpath('./table[@class="h4"]/tr')
        assert len(tr_tags) > 0, 'invalid tr_tags'

        # traverse and sanity check
        original_column_name_list = tr_tags[0].xpath('./td/text()')

        # handle the first column name: '有價證券代號及名稱'
        combined_column_name = original_column_name_list[0].strip() 
        assert combined_column_name == u'有價證券代號及名稱', 'should be 有價證券代號及名稱 in unicode'
        # the chinese character '及' means 'and' so we need to seperate this column name
        seperated_column_name_list = combined_column_name.split(u'及')
        assert len(seperated_column_name_list) == 2

        column_name_list = seperated_column_name_list + original_column_name_list[1:]
        assert len(column_name_list) == 8, 'invalid column_name_list size, should be 8'
        return column_name_list

    def __assemble_row_list(self, relative_html_object):
        # skip one row of column name list
        tr_tags = relative_html_object.xpath('./table[@class="h4"]/tr')[1:]

        row_list = []
        for tr_tag in tr_tags:
            row = self.__assemble_row(tr_tag)
            # if there is only one cell '股票' in row, skip it
            if row:
                row_list.append(row)
        return row_list

    def __assemble_row(self, relative_html_object):
        td_tags = relative_html_object.xpath('./td')

        # we could not handle empty string between td tag if we use xpath './td/text()' 
        # so we need to check each td.text one by one.
        td_texts = self.__get_lxml_text_list(td_tags)

        # if there is only one cell '股票', return None
        if len(td_texts) == 1:
            return None

        # sanity check
        assert len(td_texts) == 7

        # handle the first cell: '有價證券代號及名稱'
        # it should be seperated as stock symbol and stock name
        combined_cell = td_texts[0].strip()
        seperated_cell_list = combined_cell.split()
        assert len(seperated_cell_list) == 2

        # convert to datetime.date type
        listing_date = self.string_utils.from_local_string_to_date(td_texts[2])

        row = seperated_cell_list + [td_texts[1]] + [listing_date] + td_texts[3:]
        return row

    def __get_lxml_text_list(self, tag_list):
        text_list = []
        for tag in tag_list:
            if tag.text is None:
                text_list.append('')
            else:
                text_list.append(tag.text)
        return text_list
