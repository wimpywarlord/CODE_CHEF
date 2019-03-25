for i in range(int(input())):
    s=list(input())
    flag=0
    for j in range(0,len(s)):
        if s[j]!='.':
            for k in range(j+1,len(s)):
                if s[k]!='.' :
                    #print(j+int(s[j]),k-int(s[k]))
                    if j+int(s[j])>=k-int(s[k]):
                        flag=1
                        break
        if flag==1:
            break
    if flag==1:
        print("unsafe")
    else:
        print("safe")
                    
            
