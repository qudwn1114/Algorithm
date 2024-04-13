def solution(n):
    # 홀수일때
    answer = 0
    if n % 2 == 1:
        for i in range(n):
            if (i+1) % 2 == 1:
                answer += i+1
    # 짝수일때
    else:
        for i in range(n):
            if (i+1) % 2 == 0:
                answer += (i+1) * (i+1)
    return answer
