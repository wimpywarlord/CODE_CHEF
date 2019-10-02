n,k=map(int,input().split())
arr=list(map(int,input().split()))
for i in range(k):
    use=max(arr)
    print(use)
    for j in range(n):
        arr[j]=use-arr[j]
    print(arr)
for i in range(n):
    print(arr[i],end=" ")
    
