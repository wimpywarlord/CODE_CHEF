'''def fact(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
for i in range(0,int(input())):
    n,k=map(int,input().split())
    #print(fact(n-1))
    #print(fact(k-1))
    #print(fact(n-k))
    use1=fact(n-1)
    use2=fact(k-1)
    use3=fact(n-k)
    print(use1//(use2*use3))
    
'''
def marbles(n,k):
    a=1
    if n == k:
      print(1)
      return
    if n<k:
      print(0)
      return
    if n>k :
        for j in range(min(k-1,n-k)):
           n=n-1
           a=(a*n)//(j+1)

    print(a)
for i in range(int(input())):
    n, k= map(int,input().split(" "))
    marbles(n,k)
