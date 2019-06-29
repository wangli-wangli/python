# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']#设置输出中文

def show(year, total_Score, matriculate_Quality, college_Name):#画图
	ind = np.arange(len(total_Score))
	width = 0.35

	fig, ax = plt.subplots()
	rects1 = ax.bar(ind - width/2, total_Score, width, yerr=None, color="green", label="总分")
	rects2 = ax.bar(ind + width/2, matriculate_Quality, width, yerr=None, color="Red", label="生源质量")

	ax.set_ylabel("分值")
	ax.set_title(str(year) + "年中国最好大学分数指标")
	ax.set_xticks(ind)
	ax.set_xticklabels(college_Name, rotation=20)
	ax.legend()

	def autolabel(rects, xpos='center'):
		xpos = xpos.lower()
		ha = {'center': 'center', 'right': 'left', 'left': 'right'}
		offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}

		for rect in rects:
			height = rect.get_height()
			ax.text(rect.get_x() + rect.get_width() * offset[xpos], 1.01*height,
	                '{}'.format(height), ha=ha[xpos], va='bottom')

	autolabel(rects1, "left")
	autolabel(rects2, "right")

	plt.show()#输出