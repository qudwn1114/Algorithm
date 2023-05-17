def solution(board, moves):
    answer = 0
    arr = []
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1]:
                if arr:
                    if board[j][i-1] == arr[-1]:
                        arr.pop()
                        answer += 2
                    else:
                        arr.append(board[j][i-1])
                else:
                    arr.append(board[j][i-1])
                board[j][i-1] = 0
                break
    return answer