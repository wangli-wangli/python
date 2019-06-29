# -*- coding: utf-8 -*-
"""
Created on Sat May 18 11:15:23 2019

@author: lenovo
"""

new_list=[]
l1=[]
def fib(n):#求出各因数
    n=int(n)
    while(n!=1):
        for i in range(2,int(n)+1):
            if n%i==0:
                l1.append(i)
                n=n/i
                break
           
a=input()
fib(a)
b=len(l1)
str1=a+"="

for i in range(0,b):#将因数串连成字符串
    str1=str1+str(l1[i])
    if i==b-1:
        str1=str1+' '
    else:
        str1=str1+'*'
print(str1)