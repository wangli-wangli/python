# -*- coding: utf-8 -*-
"""
Created on Sat May 18 12:06:25 2019

@author: lenovo
"""
def root(a,b,c,d,x):
    f=1
    i=0
    while(abs(f)>0.001):

        f=(a*(x**3)+b*(x**2)+c*x+d)/(3*a*(x**2)+2*b*x+c)
        x=x-f
        i=i+1
    return x
    
str1=input()
arr1=str1.split()
a=float(arr1[0])
b=float(arr1[1])
c=float(arr1[2])
d=float(arr1[3])
x=float(arr1[4])
x1=root(a,b,c,d,x)
print(round(x1,2))

