#coding:utf-8
from bs4 import  BeautifulSoup
import requests
import re
import lxml
#用get方式抓取数据
url='http://www.cntour.cn/'
strhtml=requests.get(url)
#print(strhtml.text)
#解析网页
soup =BeautifulSoup(strhtml.text,'lxml')
data=soup.select('.newsList > li > a')
#print('数据')
#print(data)
#清洗和组织数据
print('清洗后的数据')
for item in data:
    result={
        'title':item.get_text(),
        'link':item.get('href'),
        'ID':re.findall('\d+',item.get('href'))
    }
    print(result)





