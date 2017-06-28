import pandas_datareader.data as web
import datetime

start = datetime.datetime(2017, 6, 15)
end = datetime.datetime(2017, 6, 28)

# google finance 에서는 종목코드 앞에 KRX: 를 붙여서 데이터를 가져올수 있다.
gs = web.DataReader("KRX:078930", "google", start, end)

# 세계 증시에 대한 인덱스 값을 쉽게 가져올수 있다.
nasdaq = web.DataReader("NASDAQ:NDAQ", "google", start, end)

# DataReader 통해서 일부 코스닥 종목을 가져오는데 문제가 있다.
# kakao = web.DataReader("KOSDAQ:035720", "google", start, end)

