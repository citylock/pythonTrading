import urllib
import time

from urllib.request import urlopen
from bs4 import BeautifulSoup

stockItem = '005930'

url = 'http://finance.naver.com/item/sise_day.nhn?code='+ stockItem
html = urlopen(url)
source = BeautifulSoup(html.read(), "html.parser")

maxPage=source.find_all("table",align="center")

mp = maxPage[0].find_all("td",class_="pgRR")

mpNum = int(mp[0].a.get('href')[-3:])
