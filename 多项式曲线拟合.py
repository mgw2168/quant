import numpy as np
import matplotlib.pyplot as plt

# 构造需要的数据
x = np.linspace(-5, 5, 50)
y = np.sin(x) + np.random.rand(50)


plt.scatter(x, y) # 散点图

# 使用三次方多项式拟合
params = np.polyfit(x, y, 3)
print(params)

params_func = np.poly1d(params) # 构造一个便捷多项式对象
y_predict = params_func(x)  # 根据原始的x，计算y_predict

plt.scatter(x, y)
plt.plot(x, y_predict)
plt.show()
