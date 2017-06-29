import matplotlib.pyplot as plt
import pandas_datareader.data as web
import datetime

start = datetime.datetime(2015, 1, 1)
end = datetime.datetime(2017, 6, 28)

# google finance 에서는 종목코드 앞에 KRX: 를 붙여서 데이터를 가져올수 있다.
gs = web.DataReader("KRX:078930", "google", start, end)
print (gs)

# 5일/20일 이동 평균선
ma5 = gs['Close'].rolling(window=5).mean()
ma20 = gs['Close'].rolling(window=20).mean()
ma120 = gs['Close'].rolling(window=120).mean()
print (ma5)

# 기존 dataframe 에 새로운 컬럼을 추가
gs.insert(len(gs.columns), "MA5", ma5)
gs.insert(len(gs.columns), "MA20", ma20)
gs.insert(len(gs.columns), "MA120", ma120)

plt.plot(gs.index, gs['Close'], label='Close')
plt.plot(gs.index, gs['MA5'], label='MA5')
plt.plot(gs.index, gs['MA20'], label='MA20')
plt.plot(gs.index, gs['MA120'], label='MA120')

plt.legend(loc="best")
plt.grid()
plt.show()