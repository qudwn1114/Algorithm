def solution(myString, pat):
    idx = 0
    while True:
        x = myString.find(pat, idx)
        if x == -1:
            break
        idx = x + len(pat)
    answer = myString[:idx]
        
    return answer