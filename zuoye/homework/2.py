import math
import random
cishu=int(input())#投掷的次数
count=0
m=0
count=0#落在单位圆内的次数
while m<cishu:
    x=random.uniform(-1,1)
    y=random.uniform(-1,1)
    m+=1
    juli=math.sqrt(x*x+y*y)
    if juli<=1:
        count=count+1
pai=count*4/cishu#Π的值
print(pai)


