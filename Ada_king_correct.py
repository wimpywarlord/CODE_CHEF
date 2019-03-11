'''
for i in range(int(input())):
    r,c,kkk=map(int,input().split())
    print(r,c,kkk)
    if r==1 and c==1 or r==1 and c==8 or r==8 and c==8 or r==8 and c==1:
        arr=[3,5,7,9,11,13,15]
        ans=1
        for j in range(0,kkk):
            if kkk<=7:
                ans+=arr[j]
            else:
                break
        print(ans)
    elif r==1 or c==1:
        pass
    else:
        ans=0
        arr=[5,10]

'''
for t in range(int(input())):
    c,r,k=map(int,input().split())
    c1=c+k
    if c1>8:
        c1=8
    c2=c-k
    if c2<=0:
        c2=1
    tc=(c1-c)+(c-c2)+1
    c1=r+k
    if c1>8:
        c1=8
    c2=r-k
    if c2<=0:
        c2=1
    tr=(c1-r)+(r-c2)+1
    print(tc*tr)
    
