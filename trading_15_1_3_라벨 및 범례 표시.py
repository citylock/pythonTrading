import pandas_datareader.data as web
import matplotlib.pyplot as plt

lg = web.DataReader("KRX:066570", "google")
samsung = web.DataReader("KRX:005930", "google")

plt.plot(lg.index, lg['Close'], label='LG Electronics')
plt.plot(samsung.index, samsung['Close'], label='Samsung Electronics')

plt.legend(loc='upper left')
plt.show()