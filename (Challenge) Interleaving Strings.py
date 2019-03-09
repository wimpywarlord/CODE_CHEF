n=int(input())
final=''
for i in range(n):
    temp=input()
    final+=temp
use=final
final=list(final)
final.sort()
ans=''
for i in range(0,n*n):
    for j in range(0,n*n):
        if final[i]==use[j]:
            ans+=str((j)//n+1)
            break
for i in range(0,n*n):
    print(ans[i],end=' ')
