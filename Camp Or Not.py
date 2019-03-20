for i in range(int(input())):
    days=int(input())
    problem_solved=[]
    for j in range(32):
        problem_solved.append(0)
    for j in range(days):
        di,pi=map(int,input().split())
        problem_solved[di]=pi
    #print(problem_solved)
    q=int(input())
    for j in range(q):
        deadi,reqi=map(int,input().split())
        compare=0
        for k in range(0,deadi+1):
            compare+=problem_solved[k]
        if compare>=reqi:
            print("Go Camp")
        else :
            print("Go Sleep")
            
        
