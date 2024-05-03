def solution(A, B):
    answer = 0
    if A == B:
        return answer
    l = len(A)
    for i in range(l):
        answer += 1
        A = A[l-1:] + A[:l-1]
        if A == B:
            return answer
    answer = -1
    return answer