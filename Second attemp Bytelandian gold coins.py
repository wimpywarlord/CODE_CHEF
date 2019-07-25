def calculus(n):
    if n in d.keys():
        return d[n]
    d[n] = max(n, calculus(n//2) + calculus(n//3) + calculus(n//4))
    return d[n]
d = {0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,11:11}
while(True):
    try:
        n=int(input())
        print(calculus(n))
    except:
        break
