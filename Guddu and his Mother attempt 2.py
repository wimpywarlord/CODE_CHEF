for t in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    ans=0
    for i in range(0,n):
        for j in range(0,n-i):
            use=0
            subarr=[]
            for k in range(i,n-j):
                use^=arr[k]
                subarr.append(arr[k])
            #print()
            if use==0:
                #print(subarr)
                ans+=(len(subarr)-1)
    print(ans)
