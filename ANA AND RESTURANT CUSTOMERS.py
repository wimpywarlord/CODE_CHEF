for i in range(int(input())):
    n=int(input())
    ans=1
    prev_c=0
    prev_d=0
    use=[]
    for j in range(n):
        temp=list(map(int,input().split()))
        use.append(temp)
    use=sorted(use,key = lambda x:x[0])
    #print(use)
    for j in range(n):
        if use[j][0]<=prev_d and use[j][1]>prev_d:
            prev_d=use[j][1]
        if use[j][1]>prev_d and use[j][0]>prev_d:
            #print(use[j][0],use[j][1],"#",prev_d)
            ans+=1
            prev_d=use[j][1]
            prev_c=use[j][0]
    print(ans)
            
        
