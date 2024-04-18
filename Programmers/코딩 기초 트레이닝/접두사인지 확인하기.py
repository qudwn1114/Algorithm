def solution(my_string, is_prefix):
    answer = 0
    if len(my_string) >= len(is_prefix):
        for i in range(len(is_prefix)):
            if my_string[i] != is_prefix[i]:
                return answer
        answer = 1
    
    return answer