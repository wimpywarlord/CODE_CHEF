for i in range(int(input())):
    t=int(input())
    if t==0 :
        print(0,0,1)
    elif t==2 or t==1:
        print(1,0,0)
    else:
        #print(t%26,t//26)
        use1=t%26
        use2=t//26
        if 0<use1<=2 :
            print(2**use2,0,0)
        elif  2<use1<=10:
            print(0,2**use2,0)
        elif 10<use1<=26:
            print(0,0,2**use2)
        elif use1==0:
            print(0,0,2**(use2-1))

'''
t=int(input())
while t!=0:
	n=int(input())
	x=[0,0,0]
	z=2**int(n/26)
	y=n%26
	if  y>=11:
		x[2]=z
	elif y==0:
		x[2]=2**int((n-1)/26)
	elif y<=2:
		x[0]=z
	else:
		x[1]=z
	for i in x:
		print(i,end=" ")
	print()
	t=t-1
'''
