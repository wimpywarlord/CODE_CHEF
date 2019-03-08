t=int(input())
for i in range(0,t):
    n,yyy=map(int,input().split())
    arr=list(map(int,input().split()))
    z=[]
    ctr=0
    for j in range(0,n):
        for k in range(j,n):
            z.append([])
            for l in range(j,k+1):
                #print(arr[l],end=' ')
                z[ctr].append(arr[l])
            ctr+=1
            #print()
    #print(z)
    use=[]
    for j in range(0,len(z)):
        use.append([])
        while len(use[j])<yyy:
            for k in range(0,len(z[j])):
                use[j].append(z[j][k])
    #print(use)
    for j in range(0,len(use)):
        use.sort()
    #print(use)
    flist=[]
    for j in range(0,len(z)):
        ctr=0
        for k in range(0,len(z[j])):
            if z[j][k]==use[j][yyy-1]:
                ctr+=1
        flist.append(ctr)
    #print(flist)
    ans=0
    for j in range(0,len(flist)):
        if flist[j] in z[j]:
            ans+=1
    print(ans)
                
