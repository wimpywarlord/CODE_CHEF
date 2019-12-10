##for i in range(0,int(input())):
##    n=int(input())
##    my_list = list(map(int,input().split()))
####    print(my_list)
##    xxx=len(my_list)
##    ans=0
##    for j in range(0,xxx):
##        for k in range(j+1,xxx):
##            if my_list[j]== 0:
##                if my_list[k]==0:
##                    ans+=1
####                    print(my_list[j],my_list[k])
##            if my_list[j]==2:
##                if my_list[k]==2:
##                    ans+=1
####                    print(my_list[j],my_list[k])
##    print(ans)


#ATTEMPT 2

for i in range(0,int(input())):
    n=int(input())
    my_list = list(map(int,input().split()))
##    print(my_list)
    xxx=len(my_list)
    count_zero=0
    count_two=0
    for j in range(0,xxx):
        if my_list[j]==0:
            count_zero+=1
        if my_list[j]==2:
            count_two+=1
##    print(count_zero)
##    print(count_two)
    count_zero-=1
    count_two-=1
    ans = (count_zero*(count_zero+1))//2 + (count_two*(count_two+1))//2
    print(ans)
