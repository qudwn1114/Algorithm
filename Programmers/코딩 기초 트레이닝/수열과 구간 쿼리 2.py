def solution(arr, queries):
    answer = []
    for i in queries:
        temp = []
        x = -1
        for j in arr[i[0]:i[1]+1]:
            if j > i[2]:
                temp.append(j)    
        if temp:
            x = min(temp)
        answer.append(x)
                    
    return answer