for i in range(int(input())):
    n,yyy=map(int,input().split())
    arr=list(map(int,input().split()))
    pos=n
    for j in range(0,n):
        ctr=1
        s=0
        for k in range(j,n) :
            s+=arr[k]//ctr
            #print(arr[k],s,"#")
            ctr+=1
            if s>yyy:
                break
        #print(s)
        if s<=yyy:
            pos=j
            break
    print(pos+1)   
