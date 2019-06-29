# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import math
import numpy as np
plt.rcParams['font.sans-serif']=['SimHei']	#设置字体以便支持中文
plt.rcParams['axes.unicode_minus']=False	# 显示负号

x = np.arange(0, 10, 0.1)
y1 = x ** 2
y2 = np.cos(2 * x)
y3 = y1 * y2

plt.title("同一坐标系下的函数")
plt.subplot(311)	# 三行一列中的第一行
plt.plot(x, y1, '', label="x ** 2",color="red")
plt.legend()
plt.subplot(312)	# 三行一列中的第二行
plt.plot(x, y2, 'b-.', label="cos2x",color="blue")
plt.legend()
plt.subplot(313)	# 三行一列中的第三行
plt.plot(x, y3, 'r:', label="x ** 2 * cos2x",color="green")
plt.legend()

plt.show()