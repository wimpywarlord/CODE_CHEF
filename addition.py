for i in range(0,int(input())):
    a=input()
    b=input()
    bbb=len(b)
    ptr=0
    for j in range(0,bbb):
        if b[j]=='1':
            ptr=1
    if ptr==0:
        print(0)
    else:
        if len(a)>len(b):
            xxx=len(a)-len(b)
            for j in range(0,xxx):
                b="0"+b
        if len(a)<len(b):
            xxx=len(b)-len(a)
            for j in range(0,xxx):
                a="0"+a
##        print(a)
##        print(b)
        xxx=len(a)
##        print(xxx)
        ans=1
##        x=input()
##        print(x[0])
        for j in range(xxx-1,0,-1):
##            print(a[j],b[j])
            if a[j]=='1' and b[j]=='1':
                ans=2
##                print("#")
        for j in range(xxx-1,0,-1):
##            print(a[j-1],a[j])
##            print(b[j-1],b[j])
##            print()
            if (a[j]=='1' and a[j-1]=='1' and b[j]=='1' and b[j-1]=='0') or (a[j]=='1' and a[j-1]=='0' and b[j]=='1' and b[j-1]=='1'):
                ans=3
##                print("$")
        print(ans)

