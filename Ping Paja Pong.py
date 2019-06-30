for i in range(0,int(input())):
    x,y,k=map(int,input().split())
    if (x+y)<k:
        print("Chef")
    else:
        if ((x+y)//k)%2==0:
            print("Chef")
        else:
            print("Paja")
