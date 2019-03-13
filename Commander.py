def find(arr,target):
    for i in range(0,len(arr)):
        if arr[i] <= 0:
            arr[i]=0
        else:
            arr[i]=1
    print(arr)
    low=0
    high=len(arr)
    while low!=high:
        mid=(low+high)//2
        if arr[mid]<=target:
            low= mid+1
        else:
            high=mid
    return low
    
for i in range(int(input())):
    n,q=map(int,input().split())
    arr=list(map(int,input().split()))
    for j in range(q):
        id,kkk=map(int,input().split())
        print(find(arr,kkk),end=' ')
    print()
        
