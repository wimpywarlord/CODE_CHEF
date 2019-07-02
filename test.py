t=int(input())
for i in range(0,t):
    
    over=[]
    x=input()
    n,p=x.split()
    n=int(n)
    p=int(p)
    yy=input()
    y=[]
    for i in range(0,len(yy)):
        y.append(yy[i])
    print(y)
    over=[]
    for i in range(0,n):
        over.append([])
        for j in range((i*6),(i*6)+6):
            if y[j]=='W':
                over[i].append(y[j])
            else:
                over[i].append(int(y[j]))
    print(over)
    pp=[]
    for i in range(0,p):
        pp.append(0)
    scheck=0
    for i in range(0,n):
        for j in range(0,6):
            if over[i][j]!='W':
                if over[i][j]==0:
                    pp[scheck]+=0
                elif over[i][j]==2 :
                    pp[scheck]+=2
                elif over[i][j]==4 :
                    pp[scheck]+=4
                elif over[i][j]==6 :
                    pp[scheck]+=6
                elif over[i][j]==1:
                    pp[scheck]+=1
                    if scheck%2==0:
                        scheck-=1
                        print("#1")
                    else:
                        scheck+=1
                        print("#2")
            elif over[i][j]=='W':
                 if scheck%2==0:
                     scheck-=2
                     print("#3")
                 else :
                     scheck+=1
                     print("#4")
        if scheck%2==0:
            scheck-=1
        elif scheck%2!=0:
            scheck+=1
                
    print(scheck)            
    print(pp)
    cc=1
    
    print("Case",end=' ')
    print(cc,":")
    cc=cc+1
    player=1
    for i in range(0,len(pp)):
        if pp[i]==0:
            print("Player"," ",player,":","DNB")
            player+=1
        else:
            if player==scheck:  
                print("Player"," ",player,":",pp[i],"*")
                player+=1
                if scheck%2==0:
                    print("Player"," ",player,":",pp[i-1],"*")
                    player+=1
                else:
                    print("Player"," ",player,":",pp[i+1],"*")
                    player+=1
            else:
                print("Player"," ",player,":",pp[i],"*")
                player+=1
        
        
        
