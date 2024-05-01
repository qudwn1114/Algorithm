def solution(numlist, n):
    answer = []
    arr = []
    for i in numlist:
        arr.append([abs(i-n), i])
    sorted_arr = sorted(arr, key=lambda x:(x[0],-x[1]))
    for i in sorted_arr:
        answer.append(i[1])
    return answer