for i in range(0,int(input())):
    pr1,pc1,pr2,pc2=map(int,input().split())
    if pr2>pr1:
        if pc2==pc1+1 or pc2==pc1-1:
            if (pr2-pr1)%2==0:
                print("P2")
            else:
                print("P1")
        elif pc2==pc1:
            if (pr2-pr1)%2==0:
                print("P1")
            else:
                print("P2")
        else:
            if 8-pr1<pr2-1:
                print("P2")
            elif 8-pr1>pr2-1:
                print("P1")
            else:
                print("P2")
    else:
        if 8-pr1<pr2-1:
            print("P2")
        elif 8-pr1>pr2-1:
            print("P1")
        else:
            print("P2")
                
