def solution(score):
    answer = []
    arr = []
    for i in score:
        arr.append(((i[0] + i[1])/2))
    sorted_arr = sorted(arr, reverse=True)
    for i in arr:
        answer.append(sorted_arr.index(i) + 1)
    return answer
