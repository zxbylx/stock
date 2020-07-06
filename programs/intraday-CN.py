import tushare
import pandas
import datetime
import os

def stockPriceIntraday(ticker,folder):
    # 1.get intraday data online
    intraday = tushare.get_hist_data(ticker, ktype='5')
    # 2.if the history exists, append
    file = folder + ticker + '.csv'
    if os.path.exists(file):
        history = pandas.read_csv(file, index_col=0)
        intraday.append(history)
    # 3.inverse based on index
    intraday.sort_index(inplace=True)
    intraday.index.name = 'timestamp'
    # 4.save

    intraday.to_csv(file)
    print('Intraday for [' + ticker + '] got.')

# 1. Get tickers online
tickersRawData = tushare.get_stock_basics()
tickers = tickersRawData.index.tolist()
# print(tickers)

# 2. Save the ticker list to a local file
dateToday = datetime.datetime.today().strftime('%Y%m%d')
file = '../data/TickerListCN/TickerList_' + dateToday + '.csv'
tickersRawData.to_csv(file)
print('Tickers saved.')

# 3. get stock price (intraday) for all
for i, ticker in enumerate(tickers):
    try:
        print('Intraday', i, '/', len(tickers))
        stockPriceIntraday(ticker, folder='../data/intradayCN/')
    except Exception:
        pass
    if i > 5:
        break
print('Intraday for all stocks got')