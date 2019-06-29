def isPrime(a):
    b=[2,3,5,7,11]
    iss=1
    for j in b:
        if j!=a:
          if a%j==0:
            iss=2
    return iss


def primeSum(x,y):
    sum=0
    for i in range(x,y):
        #print(i)
        if isPrime(i)==1:
           sum=sum+i
           #print(i)
    #print(sum)
    return sum


x,y =map(int, input().split())
print(primeSum(x,y))