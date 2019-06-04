t=int(input())
for i in range(0,t):
    mat=[]
    for i in range(3):
        lol=input()
        mat.append(lol)
    #print(mat)
    flag=0
    for i in range(0,3):
        for j in range(0,3):
            if (i==2 and j==0) or (i==2 and j==1) or (i==1 and j==1) or (i==1 and j==0) :
                if mat[i][j]=='l' and mat[i][j+1]=='l' and mat[i-1][j]=='l':
                    flag=1
                    break
    if flag==1:
        print("yes")
    else:
        print("no")
