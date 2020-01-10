n,q=map(int,input().split())
#print(n,q)
a = list(map(int,input().split()))
#print(a)
for i in range(0,q):
    l,r=map(int,input().split())
    l=l-1
    r=r-1
    
    signal = 0 #0 IS DECREASING.
    
    signal = 1 #1 IS INCREASING.
    if a[l]>a[l+1]:
        signal = 0
        for j in range(l,r):
            
        


    
    if i_ctr==d_ctr:
        print("YES")
    else:
        print("NO")
        
