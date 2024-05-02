def solution(bin1, bin2):
    a = int(bin1) + int(bin2)
    a = list(str(a))
    a.reverse()
    x = []
    z = 0
    for i in a:
        if z + int(i) == 3:
            x.append(1)
            z = 1
        elif z + int(i) == 2:
            x.append(0)
            z = 1
        elif z + int(i) == 1:
            x.append(1)
            z = 0
        else:
            x.append(0)
            z = 0
    if z:
        x.append(1)
    x.reverse()
    answer = ''.join(map(str, x))
    return answer


print(solution("100001","1010101"))