def solution(my_string, m, c):
    answer = ''
    idx = 1
    if m == c:
        c = 0
    for i in my_string:
        if idx % m == c:
            answer += i
        idx+=1
    return answer