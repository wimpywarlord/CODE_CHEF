n,q=map(int,input().split())
print(n,q)
arr = list(map(int,input().split()))
print(arr)
for i in range(0,q):
    l,r=map(int,input().split())
    l=l-1
    r=r-1
    print(l,r)
    for j in range(l,r+1):
        
