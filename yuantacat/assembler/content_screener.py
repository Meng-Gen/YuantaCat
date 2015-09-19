#-*- coding: utf-8 -*-

from yuantacat.assembler.assemble_error import NoRecordAssembleError
from yuantacat.assembler.assemble_error import OverQueryAssembleError
from yuantacat.assembler.assemble_error import PrivateRecordAssembleError

class ContentScreener():
    def screen(self, param):
        content = param['content']
        reducded_param = dict(param)
        reducded_param.pop('content', None)
        self.__screen_unicode(content, reducded_param)
        self.__screen_big5(content, reducded_param)

    def __screen_unicode(self, content, param):
        decoded = content.decode('utf-8', 'ignore')
        if u'查詢過於頻繁，請於稍後再查詢' in decoded:
            raise OverQueryAssembleError(param)
        if u'未公告合併營業收入(採自願公告制)' in decoded:
            raise PrivateRecordAssembleError(param)
        if u'資料庫中查無需求資料' in decoded:
            raise NoRecordAssembleError(param)
        if u'was not found on this server' in decoded:
            raise NoRecordAssembleError(param)

    def __screen_big5(self, content, param):
        decoded = content.decode('big5-hkscs', 'ignore')
        if u'查詢XML申報檔過程發生錯誤，請洽系統人員' in decoded:
            raise NoRecordAssembleError(param)
        if 'stock_symbol' in param:
            if u'查無(%s)股本形成資料' % (param['stock_symbol']) in decoded:
                raise NoRecordAssembleError(param)
            if u'查無(%s) 資產負債簡表(合併財報)（季表）資料' % (param['stock_symbol']) in decoded:
                raise NoRecordAssembleError(param)
            if u'查無(%s)資產負債表(合併財報)資料' % (param['stock_symbol']) in decoded:
                raise NoRecordAssembleError(param)
            if u'查無(%s)資產負債表（合併年表）資料' % (param['stock_symbol']) in decoded:
                raise NoRecordAssembleError(param)
            if u'查無(%s)損益表資料(合併年表)' % (param['stock_symbol']) in decoded:
                raise NoRecordAssembleError(param)
            if u'查無(%s)現金流量表資料' % (param['stock_symbol']) in decoded:
                raise NoRecordAssembleError(param)
            if u'(%s)個股代碼錯誤' % (param['stock_symbol']) in decoded:
                raise NoRecordAssembleError(param)
        if u'系統通告' in decoded:
            raise NoRecordAssembleError(param)
        if u'<p>無資料' in decoded:
            raise NoRecordAssembleError(param)
