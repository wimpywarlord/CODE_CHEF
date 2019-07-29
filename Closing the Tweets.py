n,k=map(int,input().split())
d={}
for i in range(0,n):
    d["CLICK "+str(i+1)]=0
#print(d)
dkeys=list(d.keys())
for i in range(0,k):
    ans=0
    z=input()
    if z=="CLOSEALL":
        for j in range(0,n):
            d[dkeys[j]]=0
        print(0)
    else:
        if d[z]==0:
            d[z]+=1
        else:
            d[z]=0
        for j in range(0,n):
            ans+=d[dkeys[j]]
        print(ans)
    #print(d)
    
