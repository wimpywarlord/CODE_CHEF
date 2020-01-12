# function to check string is  
# palindrome or not  
def isPalindrome(str): 
  
    # Run loop from 0 to len/2  
    for i in range(0, len(str)//2):  
        if str[i] != str[len(str)-i-1]: 
            return False
    return True
for i in range(int(input())):
    n,m=map(int,(input().split()))
    mat=[]
    total=[]
    for j in range(0,n):
        mat.append(list(map(int,input().split())))
    #print(mat)
    #print(mat[3][5])
    xxx=min(n,m)
    if xxx%2==0:
        use=xxx-1
    else:
        use=min(n,m)
    #print(use)
    for j in range(0,n):
        for hhh in range(3,use+1,2):
            for k in range(0,m-hhh + 1):    
                string = ''
                for l in range(k,k+hhh):
                    #print(j,l)
                    string += str(mat [j][l])
                if isPalindrome(string):
                    #print(string,"!",j,k+hhh//2)
                    total.append([j,k+hhh//2,hhh])
    for j in range(0,m):
        for hhh in range(3,use+1,2):
            for k in range(0,n-hhh + 1):
                string= ''
                for l in range(k,k+hhh):
                    string += str(mat[l][j])
                if isPalindrome(string):
                    #print(string,"@",k+hhh//2,j)
                    total.append([k+hhh//2,j,hhh])
    copy_check = []
    for j in total:
        if j not in copy_check:
            copy_check.append(j)
    #print(total)
    #print(len(total) - len(copy_check))
    print(len(total) - len(copy_check) + m*n)
        
    
            
            
