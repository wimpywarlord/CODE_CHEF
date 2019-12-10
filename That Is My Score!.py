for i in range(0,int(input())):
    my_dict={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}
    for j in range(0,int(input())):
        p,s = map(int,input().split())
##        print(p,s)
        if p<=8:
            if my_dict[p]<s:
                my_dict[p]=s
        ans=0
        for i in range(1,9):
            ans+=my_dict[i]
    print(ans)
