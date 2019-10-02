"""
n,k=map(int,input().split())
arr=list(map(int,input().split()))
ans1=[]
ans2=[]
for i in range(2):
    use=max(arr)
    #print(i)
    #print(use)
    for j in range(n):
        arr[j]=use-arr[j]
    #print(arr)
    if i==0:
        #print(arr)
        ans1=list(arr)
    if i==1:
        #print(arr)
        ans2=list(arr)

if k%2==1:
        print(*ans1,sep=" ")
if k%2==0:
        print(*ans2,sep=" ")
"""

n, k = map(int, input().split())
arr = [int(i) for i in input().split()]
m1 = max(arr)
first = [m1 - i for i in arr]
m2 = max(first)
second = [m2 - i for i in first]

print(first)
print(second)
if k == 0:
    print(*arr, sep=' ')
    
elif k % 2 == 1:
   print(*first, sep=' ')

else:
   print(*second, sep=' ')

