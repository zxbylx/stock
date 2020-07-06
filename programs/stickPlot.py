import pandas
import matplotlib
import mplfinance
import matplotlib.pyplot as plt

def stockPricePlot(ticker):
    history = pandas.read_csv('../data/intradayCN/' + ticker + '.csv', parse_dates=True, index_col=0)

    #收盘价
    close = history['close']
    close = close.reset_index()
    close['timestamp'] = close['timestamp'].map(matplotlib.dates.date2num)

    # 开盘、最高、最低、收盘
    ohlc = history[['open','high','low', 'close']].resample('1H').ohlc()
    # 重新设置索引
    ohlc = ohlc.reset_index()
    ohlc['timestamp'] = ohlc['timestamp'].map(matplotlib.dates.date2num)

    # 散点图
    subplot1 = plt.subplot2grid((2, 1), (0, 0), rowspan=1, colspan=1)
    subplot1.xaxis_date()
    subplot1.plot(close['timestamp'], close['close'], 'b.')
    plt.title(ticker)


    plt.show()

stockPricePlot('000839')