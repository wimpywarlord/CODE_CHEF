s=input()
ss=[]
for i in s:
    ss.append(i)
print(ss)
flag=0
for i in range(0,len(ss)):
    if i < len(ss ) - 1 :
        xx=ord(ss[i])
        yy=ord(ss[i+1])
        print(xx)
        if xx>=48 and xx<=57:
            if yy>=48 and yy<=57:
                if (int(ss[i])+int(ss[i+1]))%2!=0 :
                    flag=1
        else :
            if ss[i]!='A' or  ss[i]!='E' or ss[i]!='I' or ss[i]!='O'  or ss[i]!='U' or ss[i]!='Y' :
                flag=1
    if ord(s[len(ss)-1])>57 or ord(s[len(ss)-1])<48:
        flag=1
if flag==1:
    print("invalid")
else:
    print("valid")
