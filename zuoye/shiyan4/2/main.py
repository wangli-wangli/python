# -*- coding: utf-8 -*-
# @Author: GuoXu
# @Date:   2019-06-08 18:01:23
# @FileDescription: 豆瓣图书评论数据分析与可视化
import requests
from bs4 import BeautifulSoup
import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import imageio
import jieba

Bookdata = []
def getHTMLText(url):
	try:
		r = requests.get(url, timeout = 30)
		r.raise_for_status()
		r.encoding = "utf-8"
		return r.text
	except:
		return

def fillBookdata(soup):
	commentinfo = soup.find_all("span", 'comment-info')
	pattern = re.compile(r'user-stars allstar(\d+) rating')
	p = []
	for i in range(len(commentinfo)):	# 有的评论没有星星数，所以使用之前的语句会报错，这里进行一下判断
		if re.findall(pattern, str(commentinfo[i])) != []:
			p += re.findall(pattern, str(commentinfo[i]))
		else:
			p.append(0)
	# p = re.findall(pattern, str(commentinfo))	# 星星的数量
	comments = soup.find_all('span', 'short')	# 评论内容
	pattern1 = re.compile(r'\d{4}-\d{2}-\d{2}')	# 利用正则表达式取出评论日期
	comment_time = re.findall(pattern1, str(commentinfo))
	usefulNum = soup.find_all('span', attrs={'class':'vote-count'})	# 点赞数
	for i in range(len(commentinfo)):
		Bookdata.append([commentinfo[i].a.string, comments[i].string, comment_time[i], p[i], usefulNum[i].string])

# 获取列表中第5个元素，即点赞数所在的位置
def takeUsefulNum(list1):
	return int(list1[4])

# 获取点赞榜
def getTopByUsefulNum():
	TopList = Bookdata
	TopList.sort(key = takeUsefulNum, reverse = True)	# key代表根据之前获得的点赞数排序，reverse = True表示降序
	return TopList

def printList(alist, num):
	for i in range(num):
		u = alist[i]
		print("序号：{}\n用户名：{}\n评论内容：{}\n评论时间：{}".format(i + 1, u[0], u[1], u[2]))
		if int(u[3]) == 0:
			print("评分：暂无评分")
		else:
			print("评分：{}星".format(int(int(u[3])/10)))
		print("点赞数：{}\n".format(int(u[4])))

def main(bookid, num, pageNum, method='new'):
	for i in range(pageNum):
		url = "https://book.douban.com/subject/{}/comments/{}?p={}".format(bookid, method, i + 1)
		html = getHTMLText(url)
		soup = BeautifulSoup(html, 'html.parser')
		fillBookdata(soup)
	printList(Bookdata, num)
	print("点赞TOP10：")
	printList(getTopByUsefulNum(), 10)
	showWordCloud()

# 词云显示
def showWordCloud():
	text = ""
	for i in Bookdata:	# 利用for循环取出Bookdata中的评论
		text += i[1]
	# 利用jieba分词
	wordlist = jieba.cut(text, cut_all=True)
	wl = " ".join(wordlist)
	wc = WordCloud(
			background_color = "white",	# 背景颜色
			max_words = 2000,			# 最大显示的字数
			font_path='simfang.ttf',	# 中文字体，wordcloud不支持中文
			max_font_size = 60,			# 字体最大值
			random_state = 30,			# 有多少种随机生成状态
		)
	myword = wc.generate(wl)
	wc.to_file('result_pfdsj.jpg')

	# 展示
	plt.imshow(myword)
	plt.axis('off')
	plt.show()


if __name__ == '__main__':
	# bookId = "20492971"	# 都挺好id
	bookId = "1200840"	# 平凡的世界id
	print("请选择排序方式：1、热门 2、最新")
	choose = input()
	while choose != '1' and choose != '2':
		print("输入错误，请重新输入：")
		choose = input()
	if choose == '1':
		main(bookId, 60, 3, 'hot')
	elif choose == '2':
		main(bookId, 60, 3, 'new')
