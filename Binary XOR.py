import math 
for i in range(0,int(input())):
    n=int(input())
    a=input()
    b=input()
    a_config=[0,0]
    b_config=[0,0]
    for j in range(0,len(a)):
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
    minn=  abs(a_config[0]-b_config[0])
    maxx = min(a_config[0],b_config[1])  + min(a_config[1],b_config[0])
    #print(minn,maxx)
    ans=0
    while minn<=maxx:
        #print(len(b),minn,"$")
        #print(math.factorial(len(a))//(math.factorial(minn)*math.factorial(len(b)-minn)))
        ans+=math.factorial(len(a))//(math.factorial(minn)*math.factorial(len(b)-minn))
        minn=minn+2
    print(ans%(10**9+7))
