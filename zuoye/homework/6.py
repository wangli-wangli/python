
def triangles():
    p = [1]
    while True:
        yield p#generator函数与普通函数的差别：在执行过程中，遇到yield就中断，下次又继续执行
        p = [1] + [p[i] + p[i+1] for i in range(len(p)-1)] + [1]

def printYanghui(n):
    n1 = 0
    count=n-1
    print(' '*count,1,"")
    count = count - 1
    for t in triangles():
        if n1 != 0:
            t1 = []
            for h in t:
                t1.append(str(h))
            print(' '*count,' '.join(t1),"")
            count=count-1
        n1 = n1+ 1
        if n1 == n:
            break
n=int(input())
printYanghui(n)


