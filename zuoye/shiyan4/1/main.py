# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import numpy as np
from show import show

allUniv = []
# 获取文件内容
def getHTMLText(url):
	try:
		r = requests.get(url, timeout = 30)
		r.raise_for_status()
		r.encoding = "utf-8"
		return r.text
	except:
		return ""

# 分析网页内容并提取有用数据到恰当的数据
def fillUnivList(soup):
	data = soup.find_all("tr")
	for tr in data:
		ltd = tr.find_all("td")
		if len(ltd) == 0:
			continue
		singleUniv = []
		for td in ltd:
			singleUniv.append(td.string)
		allUniv.append(singleUniv)

# 输出爬取到的信息
def printUnivList(num):
	# print(allUniv)
	tplt = "{:^5}\t{:{ocp}^12}\t{:{ocp}^5}\t{:^5}\t{:^5}"
	#方便中文对其显示，使用中文字宽作为站字符，chr(12288)为中文空格符
	print(tplt.format("排名", "学校名称", "省市", "总分", "生源质量", ocp=chr(12288)))
	for i in range(num):
		u = allUniv[i]
		print(tplt.format(u[0], u[1], u[2], u[3], u[4], ocp = chr(12288)))

# 可视化展示
def visual(year, num):
	total_Score, matriculate_Quality, college_Name = [], [], []
	for i in range(num):
		u = allUniv[i]
		total_Score.append(float(u[3]))
		matriculate_Quality.append(float(u[4]))
		college_Name.append(u[1])
	print(tuple(total_Score))
	print(tuple(matriculate_Quality))
	print(tuple(college_Name))
	show(year, total_Score, matriculate_Quality, college_Name)

def main(url, num):
	year = url[-9:-5]
	html = getHTMLText(url)
	soup = BeautifulSoup(html, "html.parser")
	fillUnivList(soup)
	printUnivList(num)
	visual(year, num)

if __name__ == '__main__':
	url = "http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html"
	main(url, 10)