t=int(input())
for i in range(0,t):
    n=int(input())
    ans=0
    for j in range(0,n):
        price,quantity,discount=map(int,input().split())
        #print(price+(discount*price)/100)
        #print((price+(discount*price)/100)*(discount/100))
        #print(((price+(discount*price)/100)-(price+(discount*price)/100)*(discount/100)))
        #print((price) - ((price+(discount*price)/100)-(price+(discount*price)/100)*(discount/100)))
        ans+=((price) - ((price+(discount*price)/100)-(price+(discount*price)/100)*(discount/100)))*quantity
    print("{0:.9f}".format(ans))
