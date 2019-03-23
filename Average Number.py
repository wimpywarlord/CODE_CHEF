'''
t=int(input())
for i in range(0,t):
    n,kkk,v=map(int,input().split())
    arr=list(map(int,input().split()))
    #print(arr)
    flag=0
    for j in range(1,10000):
        copy=list(arr)
        if j not in arr:
            for k in range(0,kkk):
                copy.append(j)
            if sum(copy)/len(copy)==v:
                print(j)
                flag=1
                break
            #print(copy,"#")
    if flag==0:
        print(-1)

======================BAD AND PRIMITIVE BRUTE FORCE METHODE =================
'''

t=int(input())
for i in range(0,t):
    n,kkk,v=map(int,input().split())
    arr=list(map(int,input().split()))
    sss=(n+kkk)*v
    curr_sum=sum(arr)
    #print(sss,curr_sum)
    if sss<=curr_sum:
        print(-1)
    else:
        if int((sss-curr_sum)/kkk)==(sss-curr_sum)/kkk :
            print(int(sss-curr_sum)//kkk)
        else:
            print(-1)
    
