def solution(array, n):
    idx = 0
    for i in range(len(array)):
        if abs(array[i] - n) == abs(array[idx] - n):
            if array[i] < array[idx]:
                idx = i
        elif abs(array[i] - n) < abs(array[idx] - n):
            idx = i
            
    answer = array[idx]
    return answer