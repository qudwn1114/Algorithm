def solution(intStrs, k, s, l):
    answer = []
    for i in intStrs:
        x = i[s: s+l]
        if int(x) > k:
            answer.append(int(x))
    return answer