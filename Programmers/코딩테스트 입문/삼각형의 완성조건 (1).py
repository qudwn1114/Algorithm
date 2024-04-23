def solution(sides):
    if sum(sides) - max(sides) > max(sides):
        return 1
    else: 
        return 2