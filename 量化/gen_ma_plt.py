import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

np.set_printoptions(precision=1)
rand_data = np.random.rand(50)
int_data = np.random.randint(15, 20, size=50)

# 计算最大数的索引
close_data = rand_data + int_data
max_index = np.argmax(close_data)
min_index = np.argmin(close_data)


# 开始模拟生成一个k线图，每个点表示收盘价
# 计算n日移动均线
def avg_data(arr, n=5):
    ret = np.cumsum(arr, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n


x = np.arange(0, 50, 1)
plt.plot(x, close_data, "--*r")

# 在图像中标出最大最小值
max_point = "x=" + str(max_index) + ", y=" + str(close_data[max_index])
min_point = "x=" + str(min_index) + ", y=" + str(close_data[min_index])
plt.annotate(max_point, xytext=(max_index, close_data[max_index]), xy=(max_index, close_data[max_index]))
plt.annotate(min_point, xytext=(min_index, close_data[min_index]), xy=(min_index, close_data[min_index]))

# 画出移动均线
x_average = np.arange(4, 50, 1)
plt.plot(x_average, avg_data(close_data))

mpl.rcParams['font.sans-serif'] = ['SimHei']
plt.savefig('./kline_ma.jpg')
plt.show()
