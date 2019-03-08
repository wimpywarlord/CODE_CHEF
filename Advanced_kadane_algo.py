from sys import maxsize 
def maxSubArraySum(a,size): 
  
    max_so_far = -maxsize - 1
    max_ending_here = 0
    start = 0
    end = 0
    s = 0
  
    for i in range(0,size): 
  
        max_ending_here += a[i] 
  
        if max_so_far < max_ending_here: 
            max_so_far = max_ending_here 
            start = s 
            end = i 
  
        if max_ending_here < 0: 
            max_ending_here = 0
            s = i+1
    maxarr=[]
    for i in range(start,end+1):
        maxarr.append(a[i])
    ctr=0
    for i in range(start,end+1):
        del a[i-ctr]
        ctr+=1
    return maxarr
z=[]
t=int(input())
for i in range(0,t):
    n=int(input())
    arr=list(map(int,input().split()))
    while not not arr:
        z.append(maxSubArraySum(arr,len(arr)))
    arr=[]
    for i in range(0,len(z)):
        arr.append(len(z[i]))
    print(z)
    print(max(arr),min(arr))
    
