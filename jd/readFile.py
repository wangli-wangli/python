import jieba
from test2 import getMessage
#读取文件
f=open(r"F:\Python_Document\jd\JD_type.txt",'r')
s=f.read()
f.close()
#print(s)
#切割文件中的字符串
zifuchuan=s.split("\n");#按行分割
i=0
url=[]#第一页网址
name=[]#type
for ss in zifuchuan:
   if ss!='':#去掉空行
      #print(":"+ss)
      zifu=ss.split("\t")
      url.append(zifu[0])
      name.append(zifu[1])
      print(zifu[0]+"   "+zifu[1])



