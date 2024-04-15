def solution(n):
    answer = lcm(n, 6) // 6
    return answer

def gcd(x, y):
    while(y):
        x, y = y, x%y
    return x

def lcm(x, y):
    return x * y // gcd(x,y)