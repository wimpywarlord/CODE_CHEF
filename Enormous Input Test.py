n,k=map(int,input().split())
ans=0
for i in range(0,n):
    z=int(input())
    if z%k==0:
        ans+=1
print(ans)
