    
post1=int(input())
guy=list(map(int,input().split()[:post1]))
for p in range(post1):
  print(guy[p],p)
