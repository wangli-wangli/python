n1=input()
n2=input()
n3=input()
n4=input()
n5=input()
a1=list(n1)
a=[]
for j in a1:
    if j not in a:
        a.append(j)
b=n2.split(' ')
for i in b:
    if i=='':
        b.remove(i)
b.remove('')
b=sorted(b)
acm=n3.split(' ')
english=n4.split(' ')
c=b+a
p1=[]#输出两个班级中既没有参加ACM，也没有参加English的名单和数量
p2=[]#输出所有参加竞赛的人员的名单和数量
p3=[]#输出既参加了ACM，又参加了英语竞赛的所有人员及数量
p4=[]#输出参加了ACM，未参加英语竞赛的所有人员名单
p5=[]#输出参加英语竞赛，未参加ACM的所有人员名单
p6=[]#输出参加只参加ACM或只参加英语竞赛的人员名单
for i in c:
    if (i not in acm)&(i not in english):
        p1.append(i)
    if (i in acm)|(i in english):
        p2.append(i)
    if (i in acm)&(i in english):
        p3.append(i)
    if (i in acm)&(i not in english):
        p4.append(i)
    if (i not in acm)&(i in english):
        p5.append(i)
    if ((i in acm)&(i not in english))|((i not in acm)&(i in english)):
        p6.append(i)
print("Total:",len(c))#输出所有人员的数量
# print("Not in race:",p1 ,", num:",len(p1))
# print("All racers:",p2 ,", num:",len(p2))#参加所有比赛的人
# print("ACM + English:",p3 ,", num:",len(p3))
# print("Only ACM:",p4)
# print("Only English:",p5)
# print("ACM Or English:",p6)
print('Not in race: {0}, num: {1}'.format(sorted(p1),str(len(p1))))
print('All racers: {0}, num: {1}'.format(sorted(p2),str(len(p2))))
print('ACM + English: {0}, num: {1}'.format(sorted(p3),str(len(p3))))
print('Only ACM: {0}'.format(sorted(p4)))
print('Only English: {0}'.format(sorted(p5)))
print('ACM Or English: {0}'.format(sorted(p6)))
if n5 in a:
    a.remove(n5)
    #print(a)
    print(sorted(a))
elif n5 in b:
    b.remove(n5)
    #print(b)
    print(sorted(b))



