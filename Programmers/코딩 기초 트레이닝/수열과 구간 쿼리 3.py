def solution(arr, queries):
    for i in queries:
        a = arr[i[0]]
        b = arr[i[1]]
        arr[i[0]] = b
        arr[i[1]] = a
        
    return arr