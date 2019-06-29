arr1=[]#二维矩阵
max1=[]#各行最大值
min1=[]#各列最小值
for i in range(0,5):
    str2=input().split()
    list1=[int(i) for i in str2]#分割一行数据
    arr1.append(list1)
    h=0
    #查找各行最大值
    for j in list1:
        m=max(list1)
        if j==m:
            max1.append([i+1,h+1,m])
        h=h+1
   
arr2=[[arr1[j][i] for j in range(5)] for i  in range(5)]#arr2是arr1的转置矩阵
n=0
for i in arr2:
    n=n+1
    #查找各列最小值
    k=0
    for j in i:
        m=min(i)
        if j==m:
            min1.append([k+1,n,m])
        k=k+1
 
for i in max1:
    for j in min1:
        if str(i)==str(j):
            print(i,end=" ")
    
    