def solution(n):
    answer = 2
    a = n ** (1/2)
    if a == int(a):
        answer = 1
        
    return answer