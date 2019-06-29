n1=input()
n2=list(n1)
if n2[0]=='$':
  money=''.join(n2[1:])
  m=float(money)
  m2=m*6
  print('R%.2f'%m2)
if n2[0]=='R':
  money=''.join(n2[1:])
  m=float(money)
  m2=m/6
  print('$%.2f'%m2)