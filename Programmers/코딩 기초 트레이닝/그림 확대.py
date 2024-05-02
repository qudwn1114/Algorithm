def solution(picture, k):
    answer = []
    for i in picture:
        x = ''
        for j in i:
            x += j*k
        for j in range(k):
            answer.append(x)
    return answer