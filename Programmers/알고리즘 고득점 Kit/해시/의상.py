def solution(clothes):
    answer = 1
    c = {}
    for i in clothes:
        if c.get(i[1]):
            c[i[1]] += 1
        else:
            c[i[1]] = 1
    for k, v in c.items():
        answer *= v + 1
    answer -= 1
    return answer