def prime_check(num):
        if num > 1:
           for i in range(2,num):
               if (num % i) == 0:
                   break
           else:
               return 1
        else:
              return 0

for i in range(int(input())):
    z=int(input())
    n=(5*z*z+3)
    flag=0
    for j in range(2,n//2):
        if prime_check(j) and prime_check(n-j):
               flag=1
               break
    if flag==1:
               print("PRIM")
    else:
               print("NOTPRIM")
