for i in range(0,int(input())):
    a=input()
    b=input()
    if b=='0':
        print(0)
    else:
        if len(a)>len(b):
            xxx=len(a)-len(b)
            for j in range(0,xxx):
                b="0"+b
        if len(b)>len(a):
            xxx=len(b)-len(a)
            for j in range(0,xxx):
                a="0"+a
        a="0"+a
        b="0"+b
        #print(a)
        #print(b)
        xxx=len(a)
        ans_list=[]
        a=a[::-1]
        b=b[::-1]
        for j in range(0,xxx-1):
            ans=1
            if a[j]=='1' and b[j]=='1':
                #print("%",j)
                ctr=1
                while True:
                    #print(j,ctr)
                    if (a[ctr+j]=='1' and b[ctr+j]=='0') or (a[ctr+j]=='0' and b[ctr+j]=='1'):
                        ans+=1
                        #print(a[j+ctr],b[j+ctr],j+ctr)
                        #print("#")
                    else:
                        break
                    if j==xxx-2:
                        break
                    ctr+=1
                ans_list.append(ans)
        if len(ans_list)==0:
            print(1)
        else:
            #print(ans_list)
            print(max(ans_list)+1)
