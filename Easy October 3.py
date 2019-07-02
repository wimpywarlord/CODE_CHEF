xx=input()
a,k=xx.split()
a=int(a)
k=int(k)
def permutList(l):
    if not l:
            return [[]]
    res = []
    for e in l:
            temp = l[:]
            temp.remove(e)
            res.extend([[e] + r for r in permutList(temp)])

    return res
def fact(n):
    f=1
    while n>0:
       f=f*n
       n-=1
    return f
for i in range(1,a+1):
    main=[]
    for j in range(1,i+1):
        main.append(j)
    days=(fact(i)*(fact(i)-1))//2
    group=permutList(main)
    print(group)
    kill=[]
    ctr=0
    for l in range(0,len(group)):
        for m in range(l+1,len(group)):
            kill.append([])
            kill[ctr].append(group[l])
            kill[ctr].append(group[m])
            ctr+=1
    print(kill)
    if i>2:
        dad=0
        for r in range(0,len(kill)):
            mom=0
            for s in range(0,len(kill[r])):
                for t in range(0,len(kill[r][s])):
                    if kill[r][0][t]==kill[r][1][t]:
                            mom+=1
            if mom>k:
                dad+=1
        dad=dad%(10**9+7)
        print(dad)
    else:
        print(0,end=' ')
    
    
        
        
