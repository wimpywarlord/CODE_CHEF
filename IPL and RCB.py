t=int(input())
for i in range(0,t):
    p,n=map(int,input().split())
    if p<n:
        print(0)
    else:
        win=n
        score=2*win
        #print(score)
        while score!=p:
            score-=1
            win-=1
        print(win)
            
            
