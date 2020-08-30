import tushare as ts

pd_hist = ts.get_hist_data('600848')  # 一次性获取全部日k线数据
print(pd_hist)


