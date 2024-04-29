def solution(arr, n):
    x = 1
    # 홀수 일때
    if len(arr) % 2 == 1:
        x = 0
    for i in range(len(arr)):
        if i % 2 == x:
            arr[i] += n
            
    return arr