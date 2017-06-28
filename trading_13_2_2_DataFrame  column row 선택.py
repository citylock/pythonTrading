from pandas import Series, DataFrame

# example 2 : 대신 증권의 일별 시가(open), 고가(high), 저가(low), 종가(close)

daeshin = { 'open': [11650, 11100, 11200, 11100, 11000],
            'high': [12100, 11800, 11200, 11100, 11150],
            'low': [11600, 11050, 10900, 10950, 10900],
            'close':[11900, 11600, 11000, 11100, 11050]}

date = ['16.02.29', '16.02.26', '16.02.25', '16.02.24', '16.02.23']
daeshin_day = DataFrame(daeshin, columns=['open', 'high', 'low', 'close'], index=date)

close = daeshin_day['close']
print(close)

# DataFrame 의  column 선택 - error !!!!
print(daeshin_day['16.02,24'])

day_data = daeshin_day.ix['16.02.24']
print(day_data)
print(type(day_data))

# DataFrame 객체에 칼럼 이름과 인덱스 값을 확인
print(daeshin_day.index)
print(daeshin_day.columns)