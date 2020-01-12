import sys
for i in range(0,int(input())):
    N=int(input())
    A=int(input())
    S=int(2*(10**N) + A )
    print(S)
    sys.stdout.flush()
    B=input()
    C=100-int(B) 
    print(C)
    sys.stdout.flush()
    D=input()
    E= 100- int(D)
    print(E)
    sys.stdout.flush()
    XXX=input()
    if XXX=='-1':
        sys.exit()
