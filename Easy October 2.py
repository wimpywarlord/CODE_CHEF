xx=input()
t,m=xx.split()
t=int(t)
m=int(m)
yy=input()
n=yy.split()
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
for i in range(0,len(n)):
    n[i]=int(n[i])
for k in range(0,t):
    main=[]
    for l in range(1,n[k]+1):
        main.append(l)
    print(m)
    group=permutList(main)
    print(group)
    days=(fact(n[i])*(fact(n[i])-1))//2
    print(days)
    kill=[]
    ctr=0
    for i in range(0,len(group)):
        for j in range(i+1,len(group)):
            kill.append([])
            kill[ctr].append(group[i])
            kill[ctr].append(group[j])
            ctr+=1
    lol=0
    if n[k]>2:
        for i in range(0,len(kill)):
            for j in range(1):
                for k in range(0,len(kill[i][j])):
                    if kill[i][0][k]==kill[i][1][k]:
                        lol+=1
        print(kill)
        lol=lol%m
        print(lol)
    else:
        print(0)
                    
    
                    
        
    
