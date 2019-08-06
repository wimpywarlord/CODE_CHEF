for i in range(int(input())):
    n=input()
    if n=="99":
        print(101)
    elif len(n)==1:
        print(int(n)+1)
    elif len(n)==2:
        print(int(n)+11)
    else:
        base = 10**(len(n)-1) + 1
        if len(n)%2==0:
            use=11*(10**(len(n)//3))
            print(use,"$")
            while True:
                print(base,"!")
                base = base+use
                if base > int(n):
                    break
            print(base)
        else:
            use=10*(10**(len(n)//3))
            print(use,"&")
            while True:
                print(base,"@")
                base = base + use
                if base > int(n):
                    break
            print(base)


