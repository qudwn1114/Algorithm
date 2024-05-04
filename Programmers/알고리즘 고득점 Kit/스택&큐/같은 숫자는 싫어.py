def solution(arr):
    answer = []
    for i in arr:
        if not answer:
            last = i
            answer.append(i)
        else:
            if last != i:
                answer.append(i)
                last = i
    return answer