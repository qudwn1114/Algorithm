def solution(a, b):
    x = int(str(a)+str(b))
    y = int(str(b)+str(a))
    answer = x if x > y else y
    return answer