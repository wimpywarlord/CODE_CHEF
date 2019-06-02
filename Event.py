t=int(input())
mat=[[1,2,3,4,5,6,7],[7,1,2,3,4,5,6,],[6,7,1,2,3,4,5],[5,6,7,1,2,3,4],[4,5,6,7,1,2,3],[3,4,5,6,7,1,2],[2,3,4,5,6,7,1]]
d1={"saturday":6, "sunday":7, "monday":1, "tuesday":2, "wednesday":3, "thursday":4 ,"friday":5}
for i in range(0,t):
    s,e,l,r=input().split()
    l=int(l)
    r=int(r)                
    ctr=0
    lol=[]
    use=mat[d1[s]-1][d1[e]-1]
    while use <= r:
        if r>=use>=l:
            ctr+=1
            lol.append(use)
        use+=7
    if ctr==1:
        print(lol[0])
    if ctr==0:
        print("impossible")
    if ctr>1:
        print("many")
    
    
