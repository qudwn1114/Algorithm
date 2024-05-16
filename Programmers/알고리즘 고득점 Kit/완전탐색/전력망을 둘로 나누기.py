global g
global cnt

def solution(n, wires):
    answer = n - 1
    global g
    global cnt
    
    g = []
    for i in range(n):
        g.append([0] * n)
    for i in wires:
        g[i[0] - 1][i[1] - 1] = 1
        g[i[1] - 1][i[0] - 1] = 1
        
    for i in wires:
        cnt = 0
        connection_count(g, i[0] - 1, i[1] - 1)
        a = cnt
        b = n - 2 - cnt
        if answer > abs(a-b):
            answer = abs(a-b)
    
    return answer

def connection_count(g, start, x): # start: 해당노드 주변 탐색, x: 탐색에서 제외
    global cnt
    if start == 1:
        print(g[start])
    for i in range(len(g)):
        if g[start][i] == 1 and i != x:
            connection_count(g, i, start)
            cnt += 1    

print(solution(4,[[1,2],[2,3],[3,4]]))