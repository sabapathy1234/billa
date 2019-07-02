rs1=int(input())
vz1=list(map(int,input().split()[:rs1]))
vz1.sort()
for i in vz1:
  print(i,end=" ")
