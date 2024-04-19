def solution(balls, share):
    n = 1
    m =1
    for i in range(share):
        n *= (balls - i)
    for i in range(share):
        m *= (share - i)
    answer = n // m
    return answer