t=int(input())
for i in range(0,t):
    number,digit=map(int,input().split())
    number=list(str(number).strip('0'))
    for j in range(0,len(number)):
        number[j]=int(number[j])
    for j in range(0,len(number)):
        number[j]=int(number[j])
    #print(number)
    z=max(number)
    arruse=sorted(number)
    #print(arruse)
    use=[]
    curr=-1
    #print(arruse)
    for j in range(0,len(arruse)):
        for k in range(curr+1,len(number)):
            if arruse[j]==number[k]:
                if arruse[j]<digit:
                    if k>=curr:
                        use.append(k)
                        curr=k
                        break
                else:
                    break
    #print(use)
    ans=''
    for j in range(0,len(use)):
        ans+=str(number[use[j]])
    #print(ans)
    yyy=len(number)-len(use)
    for j in range(0,yyy):
        ans+=str(digit)
    print(ans)
