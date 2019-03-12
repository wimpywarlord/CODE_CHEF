t=int(input())
for i in range(0,t):
    n=int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    #print(arr)
    sum=0
    ctr=n-1
    for i in range(0,n//2):
        #print(arr[i],arr[ctr-i])
        #print(abs(arr[i]-arr[ctr-i]))
        sum+=abs(arr[i]-arr[ctr-i])
    print(sum)
    
