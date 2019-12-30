for i in range(0,int(input())):
    s=input()
    s+='*'
    xxx=len(s)
    ctr_list = []
    char_list = []
    ptr=0
    while True :
        ctr=1
        char_list.append(s[ptr])
        for k in range(ptr,xxx-1):
            if s[k]==s[k+1]:
                ptr+=1
                ctr+=1
            if s[k]!=s[k+1]:
                ptr+=1
                break
        ctr_list.append(ctr)
        if ptr==xxx-1:
            break
    #print(char_list)
    #print(ctr_list)
    yyy=len(char_list)
    ans=0
    for j in range(yyy):
        ans+=1
        ans+=len(str(ctr_list[j]))
    #print(ans,xxx)
    if xxx-1<=ans:
        print("NO")
    else:
        print("YES")
        
