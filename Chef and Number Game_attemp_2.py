t=int(input())
for i in range(0,t):
    n=int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    z=[]
    if arr[0]>=0:
        flag=1
    else:
        flag=2
    z=[]
    temp=[]
    for j in range(n):
        if arr[j]>=0 and flag==1:
            temp.append(arr[j])
            flag=1
        elif arr[j]<0 and flag==1:
            z.append(temp)
            temp=[]
            temp.append(arr[j])
            flag=2
        elif arr[j]<0 and flag==2:
            temp.append(arr[j])
            flag=2
        elif arr[j]>=0 and flag==2:
            z.append(temp)
            temp=[]
            temp.append(arr[j])
            flag=1
        if j==n-1:
            z.append(temp)
    #print(z)
    ans=[]
    use=0
    for i in range(0,len(z)):
        use+=sum(z[i])**2
        ans.append(len(z[i]))
    #print(use)
    print(max(ans),min(ans))
            
        
        
            
            
