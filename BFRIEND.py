#LINK TO https://discuss.codechef.com/t/bfriend-editorial/51060
for i in range(0,int(input())):
    n,a,b,c = map(int,input().split())
    friend_floors = list(map(int,input().split()))
    #print(friend_floors)
    #print(n,a,b,c)
    ans=[0]*(n)
    for j in range(0,n):
        #print("%")
        ans[j] = abs(b-friend_floors[j]) + abs(a-friend_floors[j]) + c
    print(min(ans))
        
            
    
