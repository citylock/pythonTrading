import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt
import matplotlib.finance as matfin
import matplotlib.ticker as ticker


start = datetime.datetime(2017, 6, 1)
end = datetime.datetime(2017, 6, 30)

skhynix = web.DataReader("KRX:000660", "google", start, end)
skhynix = skhynix[skhynix['Volume'] > 0]

day_list = []
name_list = []
for i, day in enumerate(skhynix.index):
    if day.dayofweek == 0:
        day_list.append(i)
        name_list.append(day.strftime('%m/%d'))

# day_list = range(len(skhynix))

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)

ax.xaxis.set_major_locator(ticker.FixedLocator(day_list))
ax.xaxis.set_major_formatter(ticker.FixedFormatter(name_list))


matfin.candlestick2_ohlc(ax, skhynix['Open'], skhynix['High'], skhynix['Low'], skhynix['Close'], width=0.5, colorup='r', colordown='b')

plt.show()