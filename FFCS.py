t=int(input())
for i in range(0,t):
    n=int(input())
    main=""
    use=[]
    for j in range(0,n):
        z=input()
        use.append(z)
        main+=z
    set_use=list(set(main))
    #print(set_use)
    for j in range(len(set_use)):
        flag=0
        for k in range(0,n):
            if set_use[j] not in use[k]:
                flag=1
        if flag==1:
            set_use[j]=-1
    #print(set_use)
    ans=0
    for j in range(0,len(set_use)):
        if set_use[j]!=-1:
            ans+=1
    print(ans)
            
