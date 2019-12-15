for i in range(0,int(input())):
    n=int(input())
    s=input()
    use=[]
    for j in range(n,0,-1):
        for k in range(j-1,0,-1):
            if s[j-1]==s[k-1]:
                #print(k,j,s[k-1],s[j-1])
                use.append(k+(n-j))
                break
    if not use:
        print(0)
    else:
        print(max(use))
                 
for i in range(0,int(input())):
    n=int(input())
    s=input()
    use=0
    for j in range(n,0,-1):
        for k in range(j-1,0,-1):
            if s[j-1]==s[k-1]:
                if use<k+(n-j):
                    use=(k+(n-j))
                    break
    print(use)

