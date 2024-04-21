def solution(n):
    x = 1
    answer = 1
    while(True):
        x *= answer
        if x > n:
            answer -= 1
            break
        answer += 1
        
    return answer