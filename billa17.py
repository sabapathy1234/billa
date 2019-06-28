z1=int(input())
e=len(str(z1))
a=z1
b=0 
while z1>0:
  c=z1%10
  z1=z1//10
  d=c**e
  b=b+d
if a==b: 
  print('yes')
else:
  print('no')
