import math
t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    x=abs(a-b)
    if(x==0):
        print(-1)
    else:
        count=0
        for i in range(1,int(math.sqrt(x))+1):
            if(x%i==0):
                count+=1
                if(int(x/i)!=i):
                    count+=1
        print(count)
