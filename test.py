ctr=1
while ctr<1000 :
    sumdigi=0
    use=ctr
    while use>0:
        bleh=use%10
        use=use//10
        sumdigi+=bleh
    if sumdigi%10==0:
        print(ctr)
    ctr+=1

