for i in range(int(input())):
    k=int(input())
    print((10*(2)**(k-1))%(10**9+7))
    """
    for j in range(0,10**k//2):
        use=set(list(str(j)+str(10**k-j-1)))
        #print(str(j),"___",str(10**k-j-1))
        #print(use,len(use))
        if len(use)==2:
            ans+=1
    print(ans*2)
    """
