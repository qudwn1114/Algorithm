def solution(a, d, included):
    answer = 0
    n = 0
    for i in included:
        if i:
            answer += a + d*n
        n+=1
        
    return answer