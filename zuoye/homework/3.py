a = input()
a = int(a)
i = 0
l = []
cha = 0
shuchu=[]
shuchu.append(str(a))

b = a%1000
max4 = (a - b)/1000                    #求出千位
d = b%100
max3 = (b - d)/100                     #求出百位
max1 = d%10
max2 = (d - max1)/10                #求出十位
l.append(max4)
l.append(max3)
l.append(max2)
l.append(max1)
l.sort()
max1 = int(l[0])                          #最小值
max2 = int(l[1])
max3 = int(l[2])
max4 = int(l[3])                          #最大值

while cha != 6174 :
    i = i + 1
    summax = max4 * 1000 + max3 * 100 + max2 * 10 + max1
    summin = max1 * 1000 + max2 * 100 + max3 * 10 + max4
    cha = summax - summin
    baishige = cha%1000                                                             #求出百十个位
    max4 = (cha - baishige)/1000                                                 #求出千位
    shige = baishige%100                                                            #求出十个位
    max3 = (baishige - shige)/100                                                #求出百位
    max1 = shige%10                                                                   #求出个位
    max2 = (shige - max1)/10                                                      #求出十位

    l = []                                                                                        #这个地方要把列表清零，当时没注意，在这调试了很长时间
    l.append(max4)
    l.append(max3)
    l.append(max2)
    l.append(max1)
    l.sort()
    max1 = int(l[0])            #最小值
    max2 = int(l[1])
    max3 = int(l[2])
    max4 = int(l[3])            #最大值
    shuchu.append(str(cha))
print('  '.join(shuchu))