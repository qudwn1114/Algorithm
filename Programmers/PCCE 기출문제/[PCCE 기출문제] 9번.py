def solution(board, h, w):
    answer = 0
    center = board[h][w]
    
    n = len(board)
    
    # 북쪽 체크 가능할때
    if h > 0:
        if board[h-1][w] == center:
            answer +=1
    # 남쪽 체크 가능할때
    if n -1 > h:
        if board[h+1][w] == center:
            answer +=1
    # 서쪽 체크 가능할때
    if w > 0:
        if board[h][w-1] == center:
            answer +=1        
    # 동쪽 체크 가능할때
    if n - 1 > w:
        if board[h][w+1] == center:
            answer +=1
    
    return answer