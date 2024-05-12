def solution(sizes):
    w = 0
    h = 0
    for i in sizes:
        s = sorted(i, reverse=True)
        if s[0] >= w:
            w = s[0]
        if s[1] >= h:
            h= s[1]
    answer = w*h
    return answer