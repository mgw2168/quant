import datetime

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import finance
from matplotlib.dates import date2num

plt.style.use('seaborn-talk')

# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['KaiTi']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

date_arr = pd.date_range(start='2020-05-01', end='2020-05-31', freq='D')


# 模拟K线数据
def gen_kine_data(low_price=0, high_price=20, size=30):
    rand_deci = np.random.rand(size)
    rand_price = np.random.randint(low_price, high_price, size)
    price = rand_deci + rand_price
    return price


open = gen_kine_data(20, 22, date_arr.shape[0])
high = gen_kine_data(22, 23, date_arr.shape[0])
low = gen_kine_data(18, 20, date_arr.shape[0])
close = gen_kine_data(19, 22, date_arr.shape[0])

date_column = date_arr.strftime("%Y-%m-%d")

kline_data = pd.DataFrame({'date': date_column, 'open': open, 'high': high, 'low': low, 'close': close},
                          columns=['date', 'open', 'high', 'low', 'close'], dtype=float)
# print(kline_data)

# 设置date为行索引
kline_data = kline_data.set_index('date', drop=True)
format_kline_data = list()
#
for date, row in kline_data.iterrows():
    date_ = datetime.datetime.strptime(date, "%Y-%m-%d")
    t = date2num(date_)  # 将事件转换为画图所需要的数字格式
    open, high, low, close = row
    format_kline_data.append([t, open, high, low, close])


# 计算n日移动均线
def avg_data(arr, n=5):
    ret = np.cumsum(arr, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n


# 画出K线图
fig, ax = plt.subplots()
fig.subplots_adjust()
ax.xaxis_date()

# mpl.rcParams['font.sans-serif'] = ['SimHei']
# mpl.rcParams['axes.unicode_minus'] = False
plt.title("Simulate a K-line chart of a digital currency market in May")
plt.xticks(rotation=45)
plt.xlabel("date")
plt.ylabel("prices")
# 取消图例的外边框
ax.legend(loc='upper left', frameon=False)
# K线图
finance.candlestick_ohlc(ax, format_kline_data, width=0.6, colordown='red', colorup='green')

# 均线图
l1, = plt.plot(date_arr[9:], avg_data(kline_data['close'].tolist(), n=10))
ma_5 = kline_data['close'].rolling(window=5).mean()
l2, = plt.plot(date_arr, ma_5)

plt.legend(handles=[l1, l2], labels=['MA10', 'MA5'], loc='best')

plt.show()
