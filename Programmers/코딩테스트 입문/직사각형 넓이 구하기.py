def solution(dots):
    w = 0
    h = 0
    for i in range(1,4):
        if dots[0][0] == dots[i][0] and dots[0][1] != dots[i][1]:
            h = abs(dots[0][1] - dots[i][1])
        elif dots[0][0] != dots[i][0] and dots[0][1] == dots[i][1]:
            w = abs(dots[0][0] - dots[i][0])
    answer = w * h
    return answer