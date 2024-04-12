def solution(data, ext, val_ext, sort_by):
    answer = []
    temp = []
    
    if ext == 'code':
        num = 0
    elif ext == 'date':
        num = 1
    elif ext == 'maximum':
        num = 2
    else:
        num = 3
        
    if sort_by == 'code':
        sort_num = 0
    elif sort_by == 'date':
        sort_num = 1
    elif sort_by == 'maximum':
        sort_num = 2
    else:
        sort_num = 3
    #조건에 맞는 값만 추출
    for i in data:
        if i[num] < val_ext:
            temp.append(i)
    # 정렬
    # 젤 작은 녀석 찾아서 answer에 초기화
    min = temp[0][sort_num]
    max = temp[0][sort_num]
    for i in temp:
        if i[sort_num] <= min:
            min = i[sort_num]
            min_data = i
        if i[sort_num] >= max:
            max = i[sort_num]
    answer.append(min_data)

    # 반복문 돌면서 다음에 올 작은녀석 찾기
    for i in range(len(temp) - 1):
        next_num = max
        for j in temp:
            if j[sort_num] > min and j[sort_num] <= next_num:
                next_num = j[sort_num]
                next_data = j
        min = next_num
        answer.append(next_data)

    return answer

solution([[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]], "date", 20300501, "remain")