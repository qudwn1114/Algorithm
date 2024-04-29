def solution(board):
    answer = 0
    w = len(board)
    for i in range(w):
        for j in range(w):
            if board[i][j] == 1:
                # 위 체크
                if i > 0:
                    if board[i-1][j] != 1:
                        board[i-1][j] = 2
                # 아래 체크
                if i+1 < w:
                    if board[i+1][j] != 1:
                        board[i+1][j] = 2
                # 왼쪽 체크
                if j > 0:
                    if board[i][j-1] != 1:
                        board[i][j-1] = 2
                # 오른쪽 체크
                if j+1 < w:
                    if board[i][j+1] != 1:
                        board[i][j+1] = 2
                # 왼쪽 위 체크
                if i > 0 and j > 0:
                    if board[i-1][j-1] != 1:
                        board[i-1][j-1] = 2
                # 오른쪽 위 체크
                if i > 0 and j+1 < w:
                    if board[i-1][j+1] != 1:
                        board[i-1][j+1] = 2
                # 왼쪽 아래 체크
                if i+1 < w and j > 0:
                    if board[i+1][j-1] != 1:
                        board[i+1][j-1] = 2
                # 오른쪽 아래 체크
                if i+1 < w and j+1 < w:
                    if board[i+1][j+1] != 1:
                        board[i+1][j+1] = 2
    for i in board:
        answer += i.count(0)
    return answer

print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]))