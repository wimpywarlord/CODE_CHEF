'''t=int(input())
from collections import defaultdict
for i in range(0,t):
    n=int(input())
    use=[]
    for j in range(0,n):
        z=input()
        use.append(z)
    #print(use)
    ans=0
    for j in range(0,n):
        for k in range(j,n):
            temp=''
            d1=defaultdict(int)
            temp+=use[j]+use[k]
            #print(temp)
            tempcheck=sorted(temp)
            if j!=k and tempcheck :
                #print(temp)
                for k in range(0,len(temp)):
                    d1[temp[k]]+=1
            #print(d1)
            #print(len(d1))
            if len(d1)==5:
                ans+=1
    print(ans)'''
import itertools
for i in range(int(input())):
    n=int(input())
    z=[]
    for j in range(0,n):
        s=input()
        z.append("".join(list(set(s))))
    #print(z)
    ans=0
    for a in itertools.combinations(z,2):
        #print("".join(a))
        if len(set("".join(a)))==5:
            ans+=1
    print(ans)
        
        
