for i in range(int(input())):
    n=input()
    if len(n)==1:
        print(n+1)
    else:
        if len(n)%2==0:
            if len(n)==2:
                print(n+11)
            else:
                use=(len(n)//3)*11
                print(n+use)
        else:
            if len(n)==3:
                print(n+10)
            else:
                use=(len(n)//3)*10
                print(n+use)