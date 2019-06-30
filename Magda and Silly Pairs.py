import math
for i in range(0,int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    a.sort()
    b.sort(reverse=True)
    #print(a)
    #print(b)
    ans=0
    for j in range(0,n):
        maxx=0
        use=0
        for k in range(0,n):
            if maxx<=math.floor((a[j]+b[k])/2):
                if a[j]+b[k]%2==0:
                    maxx=math.floor((a[j]+b[k])/2)
                    use=a[j]+b[k]
                    check=k
                elif a[j]+b[k]%2!=0:
                    maxx=math.floor((a[j]+b[k])/2)
                    use=a[j]+b[k]
                    check=k
            if a[j]+b[k]<=use-2:
                break
        b[check]=0
        #print(maxx,check)
        ans+=maxx
    print(ans)
