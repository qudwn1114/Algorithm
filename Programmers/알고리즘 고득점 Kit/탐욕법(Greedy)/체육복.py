def solution(n, lost, reserve):
    temp = []
    for i in lost:
        if i in reserve:
            temp.append(i)
    for i in temp:
        lost.remove(i)
        reserve.remove(i)
        
    lost.sort()
    g = 0
    for i in lost:
        if i - 1 in reserve:
            g += 1
            reserve.pop(reserve.index(i - 1))
        elif i + 1 in reserve:
            g += 1
            reserve.pop(reserve.index(i + 1))
            
    answer = n - len(lost) + g
    return answer