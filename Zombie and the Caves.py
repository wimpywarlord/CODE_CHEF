from collections import defaultdict
def updateArray(c, n): 
  
    # convert array into prefix sum array 
    for i in range(1, n): 
        c[i] += c[i - 1]

for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    copya=list(a)
    b=list(map(int,input().split()))
    c=[0]*n
    for j in range(n):
        #print(a[j])
        left=j-copya[j]+1
        right=j+copya[j]+1
        if left<=0:
            left=1
        if right>n:
            right=n
        #print(left,right,"@")
        c[left-1]+=1
        if right!=n:
            c[right]-=1
    updateArray(c,n)
    #print(c)
    d1=defaultdict(int)
    d2=defaultdict(int)
    for j in range(n):
        d1[c[j]]+=1
    for j in range(n):
        d2[b[j]]+=1
    if d1==d2:
        print("YES")
    else:
        print("NO")
    
