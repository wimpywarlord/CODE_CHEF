for i in range(0,int(input())):
    maxx=-100
    for j in range(0,int(input())):
        s,p,v = map(int,input().split())
        #print(s)
        #print(p)
        #print(v)
        if maxx< ((p//(s+1))*v):
            maxx=((p//(s+1))*v)
    print(maxx)
        
    
