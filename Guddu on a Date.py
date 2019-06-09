t=int(input())
for i in range(t):
    ctrcopy=19
    n=int(input())
    ptr=0
    while ptr<(n):
        ctr=ctrcopy
        check=str(ctrcopy)
        doublecheck=str(ctrcopy+19)
        sumdigi=0
        while ctr>0:
            use=ctr%10
            ctr=ctr//10
            sumdigi+=use
        if sumdigi%10==0 and check[len(check)-1]!='0':
            ptr+=1
            if ptr>=n:
                break
            ctrcopy+=9
        elif sumdigi%10==0 and check[len(check)-1]=='0' and check[0]==doublecheck[0]:
            ptr+=1
            if ptr>=n:
                break
            ctrcopy+=19
        elif sumdigi%10==0 and check[len(check)-1]=='0' and check[0]!=doublecheck[0]:
            ptr+=1
            if ptr>=n:
                break
            ctrcopy+=18
    print(ctrcopy)    

