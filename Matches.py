"""
for i in range(int(input())):
    n,m=map(int,input().split())
    #print(n)
    #print(m)
    if n%m==0 or m%n==0:
        print("Ari")
    else:
        ctr=0
        flag1=0
        flag2=0
        while True:
            x=n
            y=m
            if n>m:
                n=n%m
                if m%n==0 and flag1==0:
                    xxx=n+m
                    if xxx != x:
                        n+=m
                        flag1=1
                ctr+=1
                print(n,"#",m)
            else:
                m=m%n
                ctr+=1
                if n%m==0 and flag2==0:
                    yyy=m+n
                    if yyy != y:
                        m+=n
                        flag2=1
                print(n,"@",m)
            if n%m==0 or m%n==0:
                ctr+=1
                print(n,"*",m)
                break
        #print(ctr)
        if ctr%2!=0:
            print("Ari")
        else:
            print("Rich")
=================================================ATTEMPT 1=================================
"""
"""

for i in range(int(input())):
    n,m=map(int,input().split())
    #print(n)
    #print(m)
    if n%m==0 or m%n==0:
        print("Ari")
    else:
        ctr=0
        while True :
            if n>m:
                n=n-m
                ctr+=1
            elif m>n:
                m=m-n
                ctr+=1
            print(n,m)
            if n%m==0 or m%n==0:
                ctr+=1
                break
        if ctr%2!=0:
            print("Ari")
        else:
            print("Rich")
===================BOTH WANT TO MAKE SURE THAT THEY CAN HAVE THIER NEXT TURN ===============

"""


"""

for i in range(int(input())):
    n,m=map(int,input().split())
    #print(n)
    #print(m)
    if n%m==0 or m%n==0:
        print("Ari")
    else:
        ctr=0
        while True:
            qqq=n
            www=m
            if n>m:
                xxx=n%m
                if xxx!=0:
                    if m%xxx!=0:
                        n=n%m
                        ctr+=1
                        #print(n,m,"!")
                    else:
                        if n%m+m!=qqq:
                            n=n%m+m
                            ctr+=1
                            #print(n,m,"@")
                        else:
                            n=n-m
                            ctr+=1
                            #print(n,m,"#")
                else:
                    ctr+=1
                    n=n%m
                    #print(n,m,"$")
                    break
            elif m>n:
                yyy=m%n
                if yyy!=0:
                    if n%yyy!=0:
                        m=m%n
                        ctr+=1
                        #print(n,m,"%")
                    else:
                        if m%n+n!=www:
                            m=m%n+n
                            ctr+=1
                            #print(n,m,"^")
                        else:
                            m=m-n
                            ctr+=1
                            #print(n,m,"&")
                else:
                    ctr+=1
                    m=m%n
                    #print(n,m,"*")
                    break
            if m%n==0 or n%m==0:
                ctr+=1
                break
        #print(ctr)
        if ctr%2!=0:
            print("Ari")
        else:
            print("Rich")
==== ATTEMP NO 3=================================        

"""
"""
for i in range(int(input())):
    n,m=map(int,input().split())
    #print(n)
    #print(m)
    if n%m==0 or m%n==0:
        print("Ari")
    else:
        ctr=0
        while True:
            xxx=n
            yyy=m
            if n>m:
                if n%m!=0:
                    if n%m+m!=xxx:
                        n=n%m + m
                        ctr+=1
                        #print(n,m,"@")
                        if (n)%(m%(n%m))==0:
                            m=m%n
                            ctr+=2
                            #print(n,m,"***")
                            break
                    else:
                        n=n%m
                        ctr+=1
                        #print(n,m,"%")
                else:
                    ctr+=1
                    #print(n,m,"!")
                    break
            if m>n:
                if m%n!=0:
                    if m%n+n!=yyy:
                        m=m%n + n
                        ctr+=1
                        #print(n,m,"$")
                        if (m)%(n%(m%n))==0:
                            n=n%m
                            ctr+=2
                            #print(n,m,")))")
                            break
                    else:
                        m=m%n
                        ctr+=1
                        #print(n,m,"&")
                else:
                    ctr+=1
                    print(n,m,"*")
                    break
            if n%m==0 or m%n==0:
                ctr+=1
                print(n,m,"^^^^")
                break
        if ctr%2!=0:
            print("Ari")
        else:
            print("Rich")


       =======FAIL ATTEMPT 4 ==================== 
                
"""


"""
for i in range(int(input())):
    n,m=map(int,input().split())
    #print(n)
    #print(m)
    if n%m==0 or m%n==0:
        print("Ari")
    else:
        ctr=0
        flag1=0
        flag2=0
        while True:
            xxx=n
            yyy=m
            if n>m:
                if m%(n%m)==0 and n%m+m!=xxx:
                    n=n%m + m
                    ctr+=1
                    print(n,m,"!")
                if m%(n%m)==0 and n%m+m==xxx:
                    n=n%m
                    ctr+=1
                    print(n,m,")))")
                else:
                    n=n%m
                    ctr+=1
                    print(n,m,"@")
                if n%m==0 or m%n==0:
                        ctr+=1
                        print(n,m,"#")
                        break
            elif m>n:
                if n%(m%n)==0 and m%n+n!=yyy:
                    m=m%n + n
                    ctr+=1
                    print(n,m,"$")
                if n%(m%n)==0 and m%n+n==yyy:
                    m=m%n
                    ctr+=1
                    print(n,m,"&&&")
                else:
                    m=m%n
                    ctr+=1
                    print(n,m,"%")
                    if n%m==0 or m%n==0:
                        ctr+=1
                        print(n,m,"^")
                        break
            if n%m==0 or m%n==0:
                ctr+=1
                print(n,m,"&")
                break
        if ctr%2!=0:
            print("Ari")
        else:
            print("Rich")
                
                
"""


"""

for i in range(int(input())):
    n,m=map(int,input().split())
    #print(n)
    #print(m)
    if n%m==0 or m%n==0:
        print("Ari")
    else:
        ctr=0
        flag=0
        while True:
            xxx=n
            yyy=m
            if n>m:     
                if n%m+m!=xxx:
                     if flag==0 and m%(n%m)!=0:
                         if (n%m)%(m%(n%m))==0 and m%(n%m)+(n%m)==m:
                                n=n%m
                                ctr+=1
                                flag=1
                                print(n,m,"^")
                         else:
                            n=n%m+m
                            ctr+=1
                            print(n,m,"!")
                     else:
                            n=n%m+m
                            ctr+=1
                            print(n,m,"((")
                else:
                    n=n%m
                    ctr+=1
                    print(n,m,"@")
            elif m>n:
                if m%n+n!=yyy:
                    if flag==0 and n%(m%n)!=0:
                        if (m%n)%(n%(m%n))==0 and n%(m%n)+(m%n)==n:
                            m=m%n
                            ctr+=1
                            flag=1
                            print(n,m,"&")
                        else:
                            m=m%n+n
                            ctr+=1
                            print(n,m,"#")
                    else:
                            m=m%n+n
                            ctr+=1
                            print(n,m,"))")
                else:
                    m=m%n
                    ctr+=1
                    print(n,m,"$")
            if n%m==0 or m%n==0:
                ctr+=1
                print(n,m,"%%%")
                break
        if ctr%2!=0:
            print("Ari")
        else:
            print("Rich")







"""


for i in range(int(input())):
    n,m=map(int,input().split())
    #print(n)
    #print(m)
    final=[]
    if n%m==0 or m%n==0:
        print("Ari")
    else:
        temp=[]
        flag=0
        while True:
            ctr=0
            if n>m:
                while n>m:
                    n=n-m
                    ctr+=1
                    print(n,m,"@")
            else:
                while m>n:
                    m=m-n
                    ctr+=1
                    print(n,m,"%")
            if flag==0:
                temp.append(ctr)
                flag=1
                print("*")
            else:
                for j in temp:
                    for k in range(1,ctr+1):
                        final.append(j+k)
                print("$")
            temp=list(final)
            if n%m==0 or m%n==0:
                ctr+=1
                print("((")
                break
    print(final)










              
            
        
