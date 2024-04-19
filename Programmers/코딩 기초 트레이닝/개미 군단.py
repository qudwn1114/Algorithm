def solution(hp):
    answer = 0
    answer += hp // 5
    left = hp % 5
    if left > 0:
        answer += left // 3
        left = left % 3
        answer += left
    
    return answer