def solution(a, b):
    g = gcd(a,b)
    b = b // g
    while True:
        if b % 2 == 0:
            b = b // 2
        elif b % 5 == 0:
            b = b // 5
        else:
            break
    if b == 1:
        answer = 1
    else:
        answer = 2
    return answer


def gcd(x, y):
    while y > 0:
        x, y = y, x % y
    return x