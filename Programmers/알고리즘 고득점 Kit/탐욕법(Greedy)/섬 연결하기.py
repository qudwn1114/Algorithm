def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x : x[2])
    s = set([costs[0][0]])
    
    while len(s) != n:
        for i in costs:
            if i[0] in s and i[1] in s:
                continue
            if i[0] in s or i[1] in s:
                s.update([i[0], i[1]])
                answer += i[2]
                break
                
    return answer