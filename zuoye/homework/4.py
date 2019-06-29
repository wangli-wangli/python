n=int(input())#进程获得使用权的主存块数量 n。
str0=input().split(' ')#进程访问页面的次序，str型
str1=[]#进程访问页面的次序，int型
str2=[]#记录未使用次数
str3=[]#贮存块种的页面
count=0 #缺页次数
d=0
for i in str0:
    str1.append(int(i))

for i in str1:
    if(len(str3)<3):#如果储存块中没有存满，存储块添加新页面
        str2.append(0)
        str3.append(i)
        for h in range(0,len(str2)):
            if h!=len(str2)-1:
               str2[h] += 1
        count+=1
    else:
        if i in str3:#如果命中
            #print('命中：',i)
            for h in range(0,len(str2)):
                if h!=d:#除了命中的页面其他页面str2加1
                    str2[h]+=1
        else:#缺页
            max=str2[0]#最近未使用页面册数最大的
            m=0
            max_m=0
            for j in str2:
                if j>max:#找到最近最久没有使用的页面
                    max=j

                    max_m=m
                m=m+1
            str3[max_m]=i#str3中增加新的页面
            str2[max_m]=0#新的页面调用次数为0
            for h in range(0,len(str2)):
                if h!=max_m:
                   str2[h] += 1
            #print('缺页：',i)
            count+=1
    shuchu1=[]
    d+=1
    # for k in str3:
    #     shuchu1.append(str(k))
    # print("存储内的页面：",'  '.join(shuchu1))
print(count)

