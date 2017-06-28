import pandas_datareader.data as web
import matplotlib.pyplot as plt
import datetime

start = datetime.datetime(2017, 1, 1)
end = datetime.datetime(2017, 6, 28)

gs = web.DataReader("KRX:078930", "google")
nasdaq = web.DataReader("NASDAQ:NDAQ", "google")

# plt.plot(gs['Close'])
plt.plot(nasdaq.index, nasdaq['Close'])
plt.show()

# test