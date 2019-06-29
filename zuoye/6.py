def PrintFN(m, n, a):
    i = 0;
    j = 1;
    k=0;
    str=[]
    count=0
    while ((i < n) & (j < n)):
        i = i + j;
        str.append(i)
        j = i + j;
        str.append(j)
        if (i >= m)&(i<=n):
            count = count + 1
            #print(i)
        if (j >= m)&(i<=n):
            count = count + 1
            #print(j)
    print("fib(%d) = %d"%(a,str[a-1]))
    print(count)



m,n,i=input().split()
n=int(n)
m=int(m)
i=int(i)
PrintFN(m,n,i)





