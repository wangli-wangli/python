import requests
from lxml import etree
import time
import csv
import random
from User_agent import  User_Agent
class Foo:
    cou=0  # 一个user_agent爬取了的页数
    i=0
    agents =User_Agent
    #正在爬取所用'user-agent'
    using_agent='Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
# 定义函数抓取第一页以及总页数和第二页的url
def crow_first(url,name):
    print('--------------crow_first---------------------')
    if Foo.cou>=14:#如果爬取的页数等于15页数，则换一个user_agent
        if Foo.i==35:#如果所有的agent都用过来了，则再重新用一遍
            Foo.i=0
        Foo.using_agent=Foo.agents[Foo.i]
        Foo.cou=0
        Foo.i=Foo.i+1
    # 获取当前的Unix时间戳，并且保留小数点后5位
    a = time.time()
    b = '%.5f' % a
    #url = 'https://list.jd.com/list.html?cat=737,1276,739'
    head = {'authority': 'search.jd.com',
            'method': 'GET',
            'scheme': 'https',
            'user-agent': Foo.using_agent,
            'x-requested-with': 'XMLHttpRequest',
            'Cookie': 'qrsc=3; pinId=RAGa4xMoVrs; xtest=1210.cf6b6759; ipLocation=%u5E7F%u4E1C; _jrda=5; TrackID=1aUdbc9HHS2MdEzabuYEyED1iDJaLWwBAfGBfyIHJZCLWKfWaB_KHKIMX9Vj9_2wUakxuSLAO9AFtB2U0SsAD-mXIh5rIfuDiSHSNhZcsJvg; shshshfpa=17943c91-d534-104f-a035-6e1719740bb6-1525571955; shshshfpb=2f200f7c5265e4af999b95b20d90e6618559f7251020a80ea1aee61500; cn=0; 3AB9D23F7A4B3C9B=QFOFIDQSIC7TZDQ7U4RPNYNFQN7S26SFCQQGTC3YU5UZQJZUBNPEXMX7O3R7SIRBTTJ72AXC4S3IJ46ESBLTNHD37U; ipLoc-djd=19-1607-3638-3638.608841570; __jdu=930036140; user-key=31a7628c-a9b2-44b0-8147-f10a9e597d6f; areaId=19; __jdv=122270672|direct|-|none|-|1529893590075; PCSYCityID=25; mt_xid=V2_52007VwsQU1xaVVoaSClUA2YLEAdbWk5YSk9MQAA0BBZOVQ0ADwNLGlUAZwQXVQpaAlkvShhcDHsCFU5eXENaGkIZWg5nAyJQbVhiWR9BGlUNZwoWYl1dVF0%3D; __jdc=122270672; shshshfp=72ec41b59960ea9a26956307465948f6; rkv=V0700; __jda=122270672.930036140.-.1529979524.1529984840.85; __jdb=122270672.1.930036140|85.1529984840; shshshsID=f797fbad20f4e576e9c30d1c381ecbb1_1_1529984840145'
            }
    r = requests.get(url, headers=head)
    r.encoding = 'utf-8'
    html1 = etree.HTML(r.text)
    datas = html1.xpath('//li[contains(@class,"gl-item")]')
    with open('JD_'+name+'.csv', 'a', newline='', encoding='utf-8')as f:
        write = csv.writer(f)
        for data in datas:
            p_name = data.xpath('div/div[@class="p-name"]/a/em/text()')
            cc=''.join(p_name[0]).split()
            p_urll = data.xpath('div/div[@class="p-name"]/a/@href')
            print([cc,p_urll[0]])
            write.writerow([cc,p_urll[0]])
    f.close()
    count=html1.xpath('//div[contains(@class,"f-pager")]//span[contains(@class,"fp-text")]//i//text()')#总页数
    next_page=html1.xpath('//a[contains(@class,"pn-next")]//@href')#下一页的url
    pages=''+count[0]
    next_url="https://list.jd.com"+next_page[0]
    Foo.cou = Foo.cou + 1
    return pages+'  '+next_url


# 定义函数抓取第二页以及以后的商品信息
def crow_then(url,name):
    # 获取当前的Unix时间戳，并且保留小数点后5位
    a = time.time()
    b = '%.5f' % a
    if Foo.cou>=14:#如果爬取的页数等于15页数，则换一个user_agent
        if Foo.i == 35:  # 如果所有的agent都用过来了，则再重新用一遍
            Foo.i = 0
        Foo.using_agent=Foo.agents[Foo.i]
        Foo.cou=0
        Foo.i=Foo.i+1
    #url = 'https://list.jd.com/list.html?cat=737,1276,739&page=3&sort=sort_rank_asc&trans=1&JL=6_0_0#J_main'
    head = {'authority': 'search.jd.com',
            'method': 'GET',
            'scheme': 'https',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
            'Cookie': 'qrsc=3; pinId=RAGa4xMoVrs; xtest=1210.cf6b6759; ipLocation=%u5E7F%u4E1C; _jrda=5; TrackID=1aUdbc9HHS2MdEzabuYEyED1iDJaLWwBAfGBfyIHJZCLWKfWaB_KHKIMX9Vj9_2wUakxuSLAO9AFtB2U0SsAD-mXIh5rIfuDiSHSNhZcsJvg; shshshfpa=17943c91-d534-104f-a035-6e1719740bb6-1525571955; shshshfpb=2f200f7c5265e4af999b95b20d90e6618559f7251020a80ea1aee61500; cn=0; 3AB9D23F7A4B3C9B=QFOFIDQSIC7TZDQ7U4RPNYNFQN7S26SFCQQGTC3YU5UZQJZUBNPEXMX7O3R7SIRBTTJ72AXC4S3IJ46ESBLTNHD37U; ipLoc-djd=19-1607-3638-3638.608841570; __jdu=930036140; user-key=31a7628c-a9b2-44b0-8147-f10a9e597d6f; areaId=19; __jdv=122270672|direct|-|none|-|1529893590075; PCSYCityID=25; mt_xid=V2_52007VwsQU1xaVVoaSClUA2YLEAdbWk5YSk9MQAA0BBZOVQ0ADwNLGlUAZwQXVQpaAlkvShhcDHsCFU5eXENaGkIZWg5nAyJQbVhiWR9BGlUNZwoWYl1dVF0%3D; __jdc=122270672; shshshfp=72ec41b59960ea9a26956307465948f6; rkv=V0700; __jda=122270672.930036140.-.1529979524.1529984840.85; __jdb=122270672.1.930036140|85.1529984840; shshshsID=f797fbad20f4e576e9c30d1c381ecbb1_1_1529984840145'

            }
    r = requests.get(url, headers=head)
    r.encoding = 'utf-8'
    html1 = etree.HTML(r.text)
    datas = html1.xpath('//li[contains(@class,"gl-item")]')
    with open('JD_' + name + '.csv', 'a', newline='', encoding='utf-8')as f:
        write = csv.writer(f)
        for data in datas:
            p_name = data.xpath('div/div[@class="p-name"]/a/em/text()')
            cc=''.join(p_name[0]).split()
            p_urll = data.xpath('div/div[@class="p-name"]/a/@href')
            print([cc,p_urll[0]])
            write.writerow([cc,p_urll[0]])
    f.close()
    Foo.cou=Foo.cou+1

def getMessage(urll,namee):
    pages_url=crow_first(urll,namee)
    str=pages_url.split('  ')
    pages=int(str[0])
    next_url=str[1]
    next=next_url.split("&")
    for i in range(2,pages):
        try:
           url=next[0]+'&page='+'%d'%i+'&'+next[2]+'&'+next[3]+'&'+next[4]
           print('   url:   ' +url)
           crow_then(url,namee)
           print('   Finish')
        except Exception as e:
           print(e)
        i=i+1
if __name__ == '__main__':
    f = open(r"F:\Python_Document\jd\JD_type.txt", 'r')
    s = f.read()
    f.close()
    # 切割文件中的字符串
    zifuchuan = s.split("\n");  # 按行分割
    i = 0
    url = []  # 第一页网址
    name = []  # type
    for ss in zifuchuan:
        if ss != '':  # 去掉空行
            zifu = ss.split("\t")
            url.append(zifu[0])
            name.append(zifu[1])
            #print(i,":","https:"+zifu[0] + "   " + zifu[1])
            getMessage("https:"+zifu[0],zifu[1])
            i=i+1