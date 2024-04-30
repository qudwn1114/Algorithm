def solution(lines):
    arr = []
    for i in lines:
        temp = []
        for j in range(i[0]+1, i[1] +1):
            temp.append(j)
        arr.append(temp)
    x = []
    for i in range(3):
        for j in range(i+1, 3):
            for k in arr[j]:
                if k in arr[i]:
                    if k not in x:
                        x.append(k)
    answer = len(x)
    return answer