#输入
str1=input()
str2=input()
str11=str1.split()
str22=str2.split()
n=str11[0]
m=str11[1]
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

