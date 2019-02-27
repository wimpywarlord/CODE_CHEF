t=int(input())
for i in range(0,t):
    n,a,b,k=map(int,input().split())
    c=a*b
    use1=((n-a)//a)+1
    use2=((n-b)//b)+1
    use3=((n-a*b)//(a*b))+1
    if use1+use2-use3>k:
        print("Win")
    else:
        print("Lose")
    
    
    
