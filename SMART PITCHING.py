n,x,y=map(int,input().split())
shreya=list(map(int,input().split()))
janvi=list(map(int,input().split()))
#print(shreya)
#print(janvi)
use=[]
for i in range(0,n):
    if shreya[i]>janvi[i]:
        use.append([abs(shreya[i]-janvi[i]),1])
    elif shreya[i]<janvi[i]:
        use.append([abs(shreya[i]-janvi[i]),2])
    else:
        use.append([abs(shreya[i]-janvi[i]),1,2])
sorted(use,key=lambda l:l[0], reverse=True)
#print(use)
ans=0
ctrs=x
ctrj=y
for i in range(0,len(use)):
        if use[i][1]==1:
            if ctrs!=0:
                ans+=shreya[i]
                ctrs-=1
            else:
                ans+=janvi[i]
                ctrj-=1
        if use[i][1]==2:
            if ctrj!=0:
                ans+=janvi[i]
                ctrj-=1
            else:
                ans+=shreya[i]
                ctrs-=1
        
print(ans)
