def solution(n):
    answer = []
    # 초기화
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(0)
        answer.append(temp)
    
    direction = 0 #0,1,2,3
    row = 0
    col = 0
    x = 0
    
    min_row = 1
    max_row = n-1
    
    min_col = 0
    max_col = n-1
    
    while True:
        if min_row > max_row and min_col > max_col:
            break
        x += 1
        answer[row][col] = x
        # 오른쪽일 경우
        if direction == 0:
            if col == max_col:
                direction = 1
                max_col -= 1
                row += 1
            else:
                col += 1
        # 아래일 경우
        elif direction == 1:
            if row == max_row:
                direction = 2
                max_row -= 1
                col -= 1
            else:
                row += 1
        # 왼쪽일 경우
        elif direction == 2:
            if col == min_col:
                direction = 3
                min_col += 1
                row -= 1
            else:
                col -= 1
        # 위쪽일 경우
        elif direction == 3:
            if row == min_row:
                direction = 0
                min_row += 1
                col += 1
            else:
                row -= 1   
    return answer
