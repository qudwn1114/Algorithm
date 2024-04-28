def solution(arr, k):
    answer = []
    for i in arr:
        if i not in answer:
            answer.append(i)
            if len(answer) == k:
                break
    diff = k - len(answer)
    if diff > 0:
        answer += [-1] * diff
        
    return answer