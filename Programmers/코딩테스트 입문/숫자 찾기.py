def solution(num, k):
    idx = str(num).find(str(k))
    if idx != -1:
        answer = idx + 1
    else:
        answer = idx
    return answer