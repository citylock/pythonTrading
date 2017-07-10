import sys
from PyQt5.QtWidgets import *
from PyQt5.QAxContainer import *
from PyQt5.QtCore import *
import time
import datetime
import pandas as pd
import sqlite3


TR_REQ_TIME_INTERVAL = 0.4

class Kiwoom(QAxWidget):

    종목코드 = []
    종목명 = []
    일시 = []
    현재가 = []
    거래량 = []
    거래대금 = []

    def __init__(self):
        super().__init__()
        self._create_kiwoom_instance()
        self._set_signal_slots()
        self.stockItem = ''
        self.stockItemName = ''


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
            print ("connected")
        else:
            print ("disconnected")

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

        if rqname == "opt10080_req":
            self._opt10080(rqname, trcode)
        elif rqname == "opt10081_req":
            self._opt10081(rqname, trcode)

        try:
            self.tr_event_loop.exit()
        except AttributeError:
            pass


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
            time = datetime.datetime(int(date[0:4]), int(date[4:6]), int(date[6:8]), int(date[8:10]), int(date[10:12]))
            today = datetime.datetime(2017, 7, 10)

            # preday_close = self._comm_get_data(trcode, "", rqname, i, "전일종가")
            if totalprice > 1000000000 and time >= today:
                print(self.stockItem, self.stockItemName, time)
                print(date, open, high, low, close, volume, totalprice)
                self.종목코드.append(self.stockItem)
                self.종목명.append(self.stockItemName)
                self.일시.append(date[0:12])
                self.현재가.append(close)
                self.거래량.append(volume)
                self.거래대금.append(totalprice / 100000000)


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

    con = sqlite3.connect("E:\workspace\pycharm\pythonTrading\db\SysTrade.db")

    cur = con.cursor()

    cur.execute("select * from stock_basic_info where 관심 = 'Y' order by 종목코드")

    rows = cur.fetchall()

    cnt = 0
    start = 1800
    num = 300
    for row in rows:
        cnt += 1
        if ( cnt >= start and cnt < (start + num)):
            print (str(cnt), ': ', str(row))
            # 주식 분봉차트 조회 요청: opt10080
            kiwoom.stockItem = row[0]
            kiwoom.stockItemName = row[1]
            kiwoom.set_input_value("종목코드", row[0])
            kiwoom.set_input_value("틱범위", "5")
            kiwoom.set_input_value("수정주가구분", 1)
            kiwoom.comm_rq_data("opt10080_req", "opt10080", 0, "0101")
            time.sleep(TR_REQ_TIME_INTERVAL)


    stock_event_dict = {'종목코드': kiwoom.종목코드, '종목명':kiwoom.종목명, '일시':kiwoom.일시,
            '현재가': kiwoom.현재가, '거래량':kiwoom.거래량, '거래대금': kiwoom.거래대금 }

    stock_event_df = pd.DataFrame.from_dict(stock_event_dict)
    stock_event_df = stock_event_df[['종목코드', '종목명', '일시', '현재가', '거래량', '거래대금']]

    stock_event_df.to_sql('stock_event_info', con, if_exists='append', index=False)
    exit()
