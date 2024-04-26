def solution(myString, pat):
    answer = 0
    idx = 0
    while True:
        x = myString.find(pat, idx)
        if x == -1:
            break
        idx = x + 1
        answer += 1
        
    return answer