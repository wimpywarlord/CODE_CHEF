for i in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    use=0
    for j in range(n):
        use^=arr[j]
    print(use)
    if use==0:
        print(n-1)
    else:
        print(0)
