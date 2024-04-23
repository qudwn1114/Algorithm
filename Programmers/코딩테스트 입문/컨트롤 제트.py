def solution(s):
    answer = 0
    last_num = 0
    s = s.split(" ")
    for i in s:            
        if i == "Z":
            answer = answer - last_num
        else:
            answer += int(i)
            last_num = int(i)
            
    return answer