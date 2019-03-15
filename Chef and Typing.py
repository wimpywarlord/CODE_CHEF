right_hand=['j','k']
left_hand=['d','f']
for i in range(int(input())):
    n=int(input())
    ref=[]
    time_taken=0
    for j in range(0,n):
        s=input()
        main_flag=0
        for k in range(0,len(ref)):
            if s==ref[k][0]:
                main_flag=1
        if main_flag==0:
            curr_time_taken=0
            flag=0
            if s[0] in right_hand:
                flag=1              #RIGHT HAND = FLAG 1
                time_taken+=2
                curr_time_taken+=2
            if s[0] in left_hand:
                flag=0              #LEFT HAND  = FLAG 0
                time_taken+=2
                curr_time_taken+=2
            for k in range(1,len(s)):
                if s[k] in left_hand and flag==0:
                    time_taken+=4
                    curr_time_taken+=4
                    flag=0
                elif s[k] in left_hand and flag==1:
                    time_taken+=2
                    curr_time_taken+=2
                    flag=0
                elif s[k] in right_hand and flag==0:
                    time_taken+=2
                    curr_time_taken+=2
                    flag=1
                elif s[k] in right_hand and flag==1:
                    time_taken+=4
                    curr_time_taken+=4
                    flag=1
            ref.append([s,curr_time_taken]) 
        else:
            #print("$")
            for k in range(0,len(ref)):
                if ref[k][0]==s:
                    time_taken+=ref[k][1]/2
                    break
            #print(ref)
    print(int(time_taken))
'''
for _ in range(int(input())):
    l=[]
    k=[]
    for i in range(int(input())):
        s=str(input())
        if s in l:
            k.append(k[l.index(s)]/2)
        else:
            a=2
            for j in range(1,len(s)):
                if(s[j-1]=="d" or s[j-1]=="f"):
                    if(s[j]=="d" or s[j]=="f"):
                        a+=4
                    else:
                        a+=2
                else:
                    if(s[j]=="d" or s[j]=="f"):
                        a+=2
                    else:
                        a+=4
            k.append(a)
        l.append(s)
        print(int(sum(k)))
'''
