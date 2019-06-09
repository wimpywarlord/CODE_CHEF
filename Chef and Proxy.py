for i in range(int(input())):
    d=int(input())
    s=input()
    ctr=0
    for j in range(d):
        if s[j]=='P':
            ctr+=1
    if ctr/d>0.75:
        print(0)
    else:
        ptr=0
        while ctr/d<0.75:
            ctr+=1
            ptr+=1
        #print(ctr)
        #print(ptr)
        check=0
        for j in range(2,d-2):
            if s[j]=='A':
                if (s[j-1]=='P' or s[j-2]=='P') and (s[j+1]=='P' or s[j+2]=='P'): 
                    check+=1
        if check>=ptr:
            print(ptr)
        else:
            print(-1)
        
