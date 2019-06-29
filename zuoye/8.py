str1=eval(input())
print(str1)
str2=[]
for i in str1:
    if str(i) not in str2:
        str2.append(str(i))
print(' '.join(str2))