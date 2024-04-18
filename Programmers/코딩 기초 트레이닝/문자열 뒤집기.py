def solution(my_string, s, e):
    reverse_str = ''
    for i in range(e, s-1, -1):
        reverse_str += my_string[i]
        
    answer = my_string[:s] + reverse_str + my_string[e+1:]
    return answer