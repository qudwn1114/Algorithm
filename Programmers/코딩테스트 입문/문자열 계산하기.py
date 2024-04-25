def solution(my_string):
    arr = my_string.split(" ")
    plus = True
    answer = 0
    for i in arr:
        if i == '+':
            plus = True
            continue
        elif i == '-':
            plus = False
            continue
        else:
            if plus:
                answer += int(i)
            else:
                answer -= int(i)
    
    return answer