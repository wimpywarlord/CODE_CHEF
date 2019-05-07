for i in range(int(input())):
    n=int(input())
    ans=n
    while n!=0:
        ans=ans+(n-1)+(ans)*(n-1)
        n=n-1
    print(ans%(10**9+7))

