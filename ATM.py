cash,bal=map(float,input().split())
if cash%5==0 and cash+0.5<bal:
    print(format(bal-cash-0.50,".2f"))
else:
    print(format(bal,".2f"))
