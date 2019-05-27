n,q=map(int,input().split())
#print(n,q)
lista=list(map(int,input().split()))
#print(lista)
listb=list(map(int,input().split()))
#print(listb)
for i in range(0,q):
    l,r=map(int,input().split())
    ans=0
    for j in range(l,r+1):
        ans+=lista[j-1]*listb[j-1]
    print(ans)
