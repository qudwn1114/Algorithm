def solution(s):
    arr = []
    for i in s:
        if s.count(i) == 1 and i not in arr:
            arr.append(i)
    arr.sort()
    answer = ''.join(arr)
    
    return answer