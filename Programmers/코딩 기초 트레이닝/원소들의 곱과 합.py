def solution(num_list):
    answer = 0
    m = 1
    s = 0
    for i in num_list:
        m *= i
        s += i
    if m < s*s:
        answer = 1
        
    return answer