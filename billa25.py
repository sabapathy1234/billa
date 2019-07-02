    
balajisa1=int(input())
sa1=list(map(int,input().split()[:balajisa1]))
sa1.sort()
que=int((len(sa1))/2)
print(sa1[que])
