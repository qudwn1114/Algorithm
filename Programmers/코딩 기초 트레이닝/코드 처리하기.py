def solution(code):
    answer = ''
    idx = 0
    mode = True
    for i in code:
        if i == "1":
            mode = not mode
        else:
            if mode:
                if idx % 2 == 0:
                    answer += i
            else:
                if idx % 2 == 1:
                    answer += i       
        idx += 1
    if answer == '':
        answer = "EMPTY"
        
    return answer