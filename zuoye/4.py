import math
def funcos(eps,x):
    str2=str(eps).split('.')
    epss=len(str2[1])
    str1=str(x).split('.')
    xss=len(str1[1])
    k=x
    a=0
    b=1
    g=x**a/math.factorial(a)
    a=a+2
    coss=0
    while(abs(g)>=eps):
       if(b%2==1):
         coss=coss+g;
         b=b+1
       else:
           coss = coss - g;
           b = b + 1
       g=x**a/math.factorial(a)
       a=a+2
    cosss=str(round(coss,epss))
    xsss=str(round(x,xss))
    print("cos(%s) = %s"%(xsss,cosss))
eps=float(input())
x=float(input())
funcos(eps,x)