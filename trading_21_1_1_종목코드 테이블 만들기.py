import sys
from PyQt5.QtWidgets import *
from PyQt5.QAxContainer import *
from PyQt5.QtCore import *
import pandas as pd
import sqlite3


class Kiwoom(QAxWidget):
    def __init__(self):
        super().__init__()
        self._create_kiwoom_instance()
        self._set_signal_slots()

    def _create_kiwoom_instance(self):
        self.setControl("KHOPENAPI.KHOpenAPICtrl.1")

    def _set_signal_slots(self):
        self.OnEventConnect.connect(self._event_connect)

    def comm_connect(self):
        # Kiwoom 로그인 요청
        self.dynamicCall("CommConnect()")
        self.login_event_loop = QEventLoop()
        self.login_event_loop.exec_()

    def _event_connect(self, err_code):
        # login 요청에 대한 응답을 대기하는 이벤트
        if err_code == 0:
            print ("connected")
        else:
            print ("disconnected")

        self.login_event_loop.exit()

    def get_code_list_by_market(self, market):
        # 종목 리스트 요청
        # market -  0:코스피, 10: 코스닥
        code_list = self.dynamicCall("GetCodeListByMarket(QString)", market)
        code_list = code_list.split(';')
        return code_list[:-1]

    def get_master_code_name(self, code):
        code_name = self.dynamicCall("GetMasterCodeName(QString)", code)
        return code_name


if __name__ == "__main__":
    app = QApplication(sys.argv)
    kiwoom = Kiwoom()
    kiwoom.comm_connect()
    code_list = kiwoom.get_code_list_by_market('10')
    codeName_list = []
    for code in code_list:
        # print (code, end=" ")
        print (code)
        codeName = kiwoom.get_master_code_name(code)
        codeName_list.append(codeName)
        print (codeName)

    stock_code_list = { 'code': code_list, 'name': codeName_list }
    df = pd.DataFrame.from_dict(stock_code_list)
    print (df)

    con = sqlite3.connect("E:\workspace\pycharm\pythonTrading\db\kosdaq.db")
    df.to_sql('kosdaq_stock_code', con, if_exists='replace', index=False)


    print ('\nThe number of companies in KOSDAQ: ' + str(len(code_list)))
