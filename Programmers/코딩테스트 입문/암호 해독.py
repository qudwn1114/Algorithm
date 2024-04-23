def solution(cipher, code):
    answer = ''
    idx = 1
    for i in cipher:
        if idx % code == 0:
            answer += i
        idx+=1
    return answer