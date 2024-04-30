def solution(n_str):
    idx = 0
    for i in n_str:
        if i == '0':
            idx += 1
        else:
            break
    answer = n_str[idx:]
    return answer