t=int(input())
from collections import defaultdict
for i in range(0,t):
    n=int(input())
    nameset=defaultdict(int)
    totallist=[]
    for j in range(0,n):
        s=input()
        totallist.append(s)
        use=list(s.split())
        nameset[use[0]]+=1
    for j in range(0,n):
        temp=list(totallist[j].split())
        if nameset[temp[0]]>1:
            print(totallist[j])
        else:
            print(temp[0])
    
        
        
        
            
