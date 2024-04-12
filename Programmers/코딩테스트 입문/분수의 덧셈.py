def solution(numer1, denom1, numer2, denom2):
    denom = lcm(denom1, denom2)
    number = numer1 * denom/denom1 + numer2 * denom/denom2
    
    g = gcd(denom, number)
    answer = [number/g, denom/g]
    
    return answer

# 최대공약수
def gcd(x,y):
    while(y):
        x,y = y,x%y
    return x

# 최소공배수
def lcm(x,y):
    return x * y / gcd(x,y)