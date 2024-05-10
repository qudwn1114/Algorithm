def solution(citations):
    answer = 0
    citations.sort()
    l = len(citations)
    for i in range(l):
        a = l - i
        if citations[i] >= a:
            return a
    return answer