def solution(arr):
    row = len(arr)
    column = len(arr[0])
    if row > column:
        for i in arr:
            for j in range(row-column):
                i.append(0)
    else: 
        for i in range(column - row):
            arr.append([0] * column)
    return arr