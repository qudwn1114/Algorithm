def solution(a, b):
    x = int(str(a)+str(b))
    y = 2 * a * b
    answer = x if x >= y else y
    
    return answer