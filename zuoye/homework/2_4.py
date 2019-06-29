# -*- coding: utf-8 -*-

class Cexception(Exception):    # 创建一个新的exception类来抛出自己的异常。
    # 异常应该继承自 Exception 类，包括直接继承，或者间接继承
    def __init__(self, errorinfor):
        self.error = errorinfor
       
    def __str__(self):
        return self.error

#def score():
 #   grade = int(input('你的成绩是：'))
 #   if grade <= 0 or grade >= 150:
  #      raise Cexception('考试分数只能在0-150')
#try:
 #   score()
#except InputError as e:
 #   print(e)
str1=input()
str2=input()
str11=str1.split()
str22=str2.split()
if len(str11)!=2:
     raise Cexception("没有输入m")
n=str11[0]
m=str11[1]
if n.isalpha()==flase:
    raise Cexception(n+"不是整数")
else:
    if(int(n)<1)|(int(n)>26):
       raise Cexception(n+"小于1或大于26")
if m>n:
    raise Cexception("m大于n")
if len(str22)>n|len(str22)<n:
    raise Cexception("输入的字符个数不是n")
    
biaoji=""
paixu=[]
zuhe=[]
#计算排列数列
for j in str22:
    biaoji=j
    for k in str22:
        if k!=biaoji:
            paixu.append(biaoji+"  "+k)
#计算组合数列
for jj in range(0,len(str22)):
    biaoji = str22[jj]
    for k in range(jj,len(str22)):
        if str22[k] != biaoji:
            zuhe.append(biaoji + "  " + str22[k])
#输出
print("Permutation:")
for h in paixu:
    print(h)
print("Combination:")
for h in zuhe:
    print(h)


