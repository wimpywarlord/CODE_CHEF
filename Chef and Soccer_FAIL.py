# CONVERT ALL THE 2's TO 1 IN WHICH + 2 WILL RESULT IN GOAL
#THE FIRST NUMBER HAS VALUE + 1 WAYS TO PASS
# REST JUST ADD WITH VALUE
t=int(input())
for i in range(0,t):
    n=int(input())
    arr=list(map(int,input().split()))
    if n==1:
        print(1)
    else:
        ans=0
        ans+=n
        #print(arr)
        for j in range(0,n):
            if arr[j]==2:
                
                    
        print(ans)
        
