import sys
for i in range(0,int(input())):
    N=int(input())
    A=int(input())
    S=int(2*(10**N) + A - 2)
    print(S)
    sys.stdout.flush()
    B=input()
    C=''
    for j in B:
        C+= str(9 - int(j))
    print(C)
    sys.stdout.flush()
    D=input()
    E=''
    for j in D:
        E+= str(9 - int(j))
    print(E)
    sys.stdout.flush()
    XXX=input()
    if XXX=='-1':
        sys.exit()
