def solution(my_str, n):
    answer = []
    s = ''
    for i in my_str:
        s += i
        if len(s) == n:
            answer.append(s)
            s = ''
    if s:
        answer.append(s)
    return answer