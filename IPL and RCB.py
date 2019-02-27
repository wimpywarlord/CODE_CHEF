t=int(input())
for i in range(0,t):
    p,n=map(int,input().split())
    while n*2>p:
        n-=1
    print(n)
        
