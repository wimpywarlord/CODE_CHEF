import math 
for i in range(0,int(input())):
    n=int(input())
    a=input()
    b=input()
    a_config=[0,0]
    b_config=[0,0]
    for j in range(0,n):
        if a[j]=='0':
            a_config[0]+=1
        if a[j]=='1':
            a_config[1]+=1
        if b[j]=='0':
            b_config[0]+=1
        if b[j]=='1':
            b_config[1]+=1
    #print(a_config)
    #print(b_config)
    minn=  abs(a_config[0]-b_config[1])
    maxx = min(a_config[0],b_config[1])  + min(a_config[1],b_config[0])
    #print(minn,maxx)
    ans=0
    while minn<=n:
        #print(math.factorial(n)//(math.factorial(minn)*math.factorial(n-minn)))
        ans+=math.factorial(n)//(math.factorial(minn)*math.factorial(n-minn))
        minn=minn+2
    print(ans%(10**9+7))
