t=int(input())
for i in range(0,t):
    n=int(input())
    attack=list(map(int,input().split()))
    defence=list(map(int,input().split()))
    ans=[]
    for j in range(1,n-1):
        if defence[j]>attack[j+1]+attack[j-1]:
            ans.append(defence[j])
    if defence[0]>attack[n-1]+attack[1]:
        ans.append(defence[0])
    if defence[n-1]>attack[0]+attack[n-2]:
        ans.append(defence[-1])
    if not ans:
        print(-1)
    else: 
        print(max(ans))
