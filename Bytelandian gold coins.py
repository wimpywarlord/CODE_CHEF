from sys import stdin
import math
for line in stdin:
    n=int(line)
    flag1=True
    flag2=True
    flag3=True
    ctr1=0
    ctr2=0
    ctr3=0
    l1=[]
    l2=[]
    l3=[]
    if n//2>=12:
        l1.append(n//2)
    if n//3>=12:
        l2.append(n//3)
    if n//4>=12:
        l3.append(n//4)
    print(l1,l2,l3)
    while True:
        #print(flag1,flag2,flag3)
        if flag1==True and len(l1)>0:
            #print(ctr1)
            #print(l1[ctr1])
            inter1=math.floor(l1[ctr1]//2)
            if inter1>=12:
                ctr1+=1
                l1.append(inter1)
            else:
                flag1=False
        if len(l1)==0:
            #print("#")
            flag1=False
        if flag2==True and len(l2)>0:
            inter2=math.floor(l2[ctr2]//3)
            if inter2>=12:
                ctr2+=1
                l2.append(inter2)
            else:
                flag2=False
        if len(l2)==0:
            flag2=False
        if flag3==True and len(l3)>0:
            inter3=math.floor(l3[ctr3]//4)
            if inter3>=12:
                ctr3+=1
                l3.append(inter3)
            else:
                flag3=False
        if len(l3)==0:
            flag3=False
        if flag1==False and flag2==False and flag3==False:
            break
    print(l1,l2,l3)
    ans=math.floor(n/2)+math.floor(n/3)+math.floor(n/4)
    print(ans,"!")
    for i in range(0,len(l1)):
        ans+=(math.floor(l1[i]/2)+math.floor(l1[i]/3)+math.floor(l1[i]/4))-l1[i]
        print(ans,"!")
    for i in range(0,len(l2)):
        ans+=((math.floor(l2[i]/2)+math.floor(l2[i]/3)+math.floor(l2[i]/4)))-l2[i]
        print(ans,"@")
    for i in range(0,len(l3)):
        ans+=((math.floor(l3[i]/2)+math.floor(l3[i]/3)+math.floor(l3[i]/4)))-l3[i]
        print(ans,"#")
    print(ans)
        
        
        


