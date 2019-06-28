s,f11=map(int,input().split())
for i in range(s + 1,f11):
  if i > 1:
    for y in range(2,i):
      if(i % y) == 0:
        break
    else:
      print(i,end=" ")
