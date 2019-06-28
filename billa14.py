n,q11=map(int,input().split())
if(q11<=100000):
    for x in range(n+1,q11):
        if(x%2!=0):
          print(x,end=" ")
