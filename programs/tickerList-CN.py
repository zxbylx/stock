import tushare
import pandas
import datetime

# 1. Get tickers online
tickersRawData = tushare.get_stock_basics()
tickers = tickersRawData.index.tolist()
print(tickers)

# 2. Save the ticker list to a local file
dateToday = datetime.datetime.today().strftime('%Y%m%d')
file = '../data/TickerListCN/TickerList_' + dateToday + '.csv'
tickersRawData.to_csv(file)
print('Tickers saved.')
