def solution(my_strings, parts):
    answer = ''
    for i in range(len(my_strings)):
        my_string = my_strings[i]
        part = parts[i]
        answer += my_string[part[0]:part[1]+1]
        
    return answer