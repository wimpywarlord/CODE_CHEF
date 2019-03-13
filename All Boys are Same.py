n,k=map(int,input().split())
arr=list(map(int,input().split()))
for i in range(0,n):
    if i+k<=n:
        sum=0
        for j in range(i,i+k):
            sum+=arr[j]
        mean=sum//k
        use=0
        for j in range(i,i+k):
            use+=(mean-arr[j])**2
        print((use/k)**(1/2))
        #print()
    else:
        break
