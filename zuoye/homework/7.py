# -*- coding: utf-8 -*-
"""
Created on Wed May 15 15:17:26 2019

@author: lenovo
"""
n=int(input())
m=int(input())
a=[]
iss=True
for i in range(n,m+1):
    iss=True
    for j in range(2,i):
        if i%j==0:
            iss=False
            break
        
    if (i not in a)&(iss==True):
        a.append(str(i))

print('  '.join(a[:5]))
print('  '.join(a[5:]))
           
    
