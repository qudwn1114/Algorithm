def solution(arr):
    n = 1
    arr_len = len(arr)
    while n < arr_len:
        n *= 2
    answer = arr + [0] * (n - arr_len)

    return answer