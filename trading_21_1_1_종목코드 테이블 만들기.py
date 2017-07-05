import sys
from PyQt5.QtWidgets import *
from PyQt5.QAxContainer import *
from PyQt5.QtCore import *
import time
import datetime
import pandas as pd
import sqlite3

TR_REQ_TIME_INTERVAL = 0.2


class Kiwoom(QAxWidget):
    def __init__(self):
        super().__init__()
        self._create_kiwoom_instance()
        self._set_signal_slots()

    def _create_kiwoom_instance(self):
        self.setControl("KHOPENAPI.KHOpenAPICtrl.1")

    def _set_signal_slots(self):
        self.OnEventConnect.connect(self._event_connect)
        self.OnReceiveTrData.connect(self._receive_tr_data)

    def comm_connect(self):
        self.dynamicCall("CommConnect()")
        self.login_event_loop = QEventLoop()
        self.login_event_loop.exec_()

    def _event_connect(self, err_code):
        if err_code == 0:
            print("connected")
        else:
            print("disconnected")

        self.login_event_loop.exit()

    def get_code_list_by_market(self, market):
        code_list = self.dynamicCall("GetCodeListByMarket(QString)", market)
        code_list = code_list.split(';')
        return code_list[:-1]

    def get_master_code_name(self, code):
        code_name = self.dynamicCall("GetMasterCodeName(QString)", code)
        return code_name

    def set_input_value(self, id, value):
        self.dynamicCall("SetInputValue(QString, QString)", id, value)

    def comm_rq_data(self, rqname, trcode, next, screen_no):
        self.dynamicCall("CommRqData(QString, QString, int, QString", rqname, trcode, next, screen_no)
        self.tr_event_loop = QEventLoop()
        self.tr_event_loop.exec_()

    def _comm_get_data(self, code, real_type, field_name, index, item_name):
        ret = self.dynamicCall("CommGetData(QString, QString, QString, int, QString", code,
                               real_type, field_name, index, item_name)
        return ret.strip()

    def _get_repeat_cnt(self, trcode, rqname):
        ret = self.dynamicCall("GetRepeatCnt(QString, QString)", trcode, rqname)
        return ret

    def _receive_tr_data(self, screen_no, rqname, trcode, record_name, next, unused1, unused2, unused3, unused4):
        if next == '2':
            self.remained_data = True
        else:
            self.remained_data = False

        if rqname == "opt10001_req":
            self._opt10001(rqname, trcode)
        elif rqname == "opt10080_req":
            self._opt10080(rqname, trcode)
        elif rqname == "opt10081_req":
            self._opt10081(rqname, trcode)

        try:
            self.tr_event_loop.exit()
        except AttributeError:
            pass

    def _opt10001(self, rqname, trcode):
        print ('LOG IN ::: opt10001 function =======')
        stockName = self._comm_get_data(trcode, "", rqname, 0, "종목명")
        print (stockName)


    def _opt10080(self, rqname, trcode):
        data_cnt = self._get_repeat_cnt(trcode, rqname)

        for i in range(data_cnt):
            date = self._comm_get_data(trcode, "", rqname, i, "체결시간")
            open = abs(int(self._comm_get_data(trcode, "", rqname, i, "시가")))
            high = abs(int(self._comm_get_data(trcode, "", rqname, i, "고가")))
            low = abs(int(self._comm_get_data(trcode, "", rqname, i, "저가")))
            close = abs(int(self._comm_get_data(trcode, "", rqname, i, "현재가")))
            volume = abs(int(self._comm_get_data(trcode, "", rqname, i, "거래량")))
            totalprice = (high + low) / 2 * volume
            # 2017 06 29 09 05 00
            time = datetime.datetime(int(date[0:4]), int(date[4:6]), int(date[6:8]))
            today = datetime.datetime(2017, 7, 3)

            # preday_close = self._comm_get_data(trcode, "", rqname, i, "전일종가")
            if totalprice > 1000000000 and time >= today:
                print(date, open, high, low, close, volume, totalprice)

    def _opt10081(self, rqname, trcode):
        data_cnt = self._get_repeat_cnt(trcode, rqname)

        for i in range(data_cnt):
            date = self._comm_get_data(trcode, "", rqname, i, "일자")
            open = self._comm_get_data(trcode, "", rqname, i, "시가")
            high = self._comm_get_data(trcode, "", rqname, i, "고가")
            low = self._comm_get_data(trcode, "", rqname, i, "저가")
            close = self._comm_get_data(trcode, "", rqname, i, "현재가")
            volume = self._comm_get_data(trcode, "", rqname, i, "거래량")
            print(date, open, high, low, close, volume)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    kiwoom = Kiwoom()
    kiwoom.comm_connect()
    today = time.strftime("%Y%m%d %H:%M:%S")

    # 1. 코스닥 종목 리스트 받아오기
    '''
    code_list = kiwoom.get_code_list_by_market('10')
    codeName_list = []
    for code in code_list:
        # print (code, end=" ")
        print(code)
        codeName = kiwoom.get_master_code_name(code)
        codeName_list.append(codeName)
    
    stock_code_list = {'code': code_list, 'name': codeName_list, 'market': '10', 'ins_date': today}
    stock_code_df = pd.DataFrame.from_dict(stock_code_list)
    # print (stock_code_df)
    
    con = sqlite3.connect("E:\workspace\pycharm\pythonTrading\db\SysTrade.db")
    stock_code_df = stock_code_df[['code', 'name', 'market', 'ins_date']]
    stock_code_df.to_sql('stock_code', con, if_exists='replace', index=False)
    
    # 2. 코스피 종목 정보 가져오기
    codeName_list = []
    stock_code_kospi = kiwoom.get_code_list_by_market('0')
    for code in stock_code_kospi:
        codeName = kiwoom.get_master_code_name(code)
        codeName_list.append(codeName)
    stock_code_kospi_dic = {'code': stock_code_kospi, 'name': codeName_list, 'market': '0', 'ins_date': today}
    stock_code_kospi_df = pd.DataFrame.from_dict(stock_code_kospi_dic)
    
    print(stock_code_kospi_df)
    stock_code_kospi_df.to_sql('stock_code', con, if_exists='append', index=False)
    '''

    # 3. 종목 기본 정보 가져오기
    kiwoom.set_input_value('종목코드', '264900')
    kiwoom.comm_rq_data("opt10001_req", "opt10001", 0, "0101")

    # print ('\nThe number of companies in KOSDAQ: ' + str(len(code_list)))
