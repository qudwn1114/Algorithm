def solution(arr, queries):
    for i in queries:
        idx = i[0]
        for j in arr[i[0]:i[1]+1]:
            if idx % i[2] == 0:
                arr[idx] += 1
            idx += 1
                
    return arr