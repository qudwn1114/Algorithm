def solution(n):
    answer = []
    for i in range(n):
        x=[]
        for j in range(n):
            if i == j:
                x.append(1)
            else:
                x.append(0)
        answer.append(x)
    return answer