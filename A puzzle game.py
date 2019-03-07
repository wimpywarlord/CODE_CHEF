#WHO SAYS THIS SHIT IS EASY...
testcases = []
for t in range(int(input())):
    input()
    a = list(map(int, input().split()))
    a += list(map(int, input().split()))
    a += list(map(int, input().split()))
    testcases.append(tuple(a))

p = [3, 5, 7, 11, 13, 17]

moves = ((0,1),(1,2),(0,3),(1,4),(2,5),(3,4),
         (4,5),(3,6),(4,7),(5,8),(6,7),(7,8))

visited = {(1,2,3,4,5,6,7,8,9):0}
states = [[1,2,3, 4,5,6,7,8,9]]

while states:
    s = states.pop(0)
    print
    for i in moves:
        if s[i[0]]+s[i[1]] in p:
                s2 = s[:]
                s2[i[0]], s2[i[1]] = s2[i[1]], s2[i[0]]
                if tuple(s2) not in visited:
                    visited[tuple(s2)] = visited[tuple(s)]+1
                    states.append(s2)

for t in testcases:
    if t in visited:
        print(visited[t])
    else:
        print(-1)
