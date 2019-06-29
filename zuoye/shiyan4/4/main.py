# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import math
from math import sqrt
import numpy as np
plt.rcParams['font.sans-serif']=['SimHei']	#设置字体以便支持中文
plt.rcParams['axes.unicode_minus']=False	# 显示负号

def f(x):
	return np.sqrt(2 * np.sqrt(x ** 2) - x ** 2)

def g(x):
	return -2.14 * (np.sqrt(np.sqrt(2) - np.sqrt(abs(x))))

x = np.arange(-2, 3)

plt.plot(x, f(x), label="f(x)",color="green")
plt.legend()
plt.plot(x, g(x), label="g(x)",color="red")
plt.legend()
xf = x[np.where((x>=-2) & (x<=2))]
plt.fill_between(xf, f(xf), g(xf), color='black', alpha=0.25)

plt.show()
