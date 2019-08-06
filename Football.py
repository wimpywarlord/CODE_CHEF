for i in range(0,int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=[0]*n
    for i in range(0,n):
        c[i]=(a[i]*20 - b[i]*10) if  (a[i]*20 - b[i]*10)>0 else 0
    print(max(c))
