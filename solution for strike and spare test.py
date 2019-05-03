import math
t=int(input())
for lol in range(t):
    n=int(input())
    if(n%2):
        p=10**(n//2)*10
    else:
        p=10**(n//2)
    q=10**n
    g=math.gcd(p,q)
    p/=g
    q/=g
    print(int(p),int(q))
