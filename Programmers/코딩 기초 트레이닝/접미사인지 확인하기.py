def solution(my_string, is_suffix):
    answer = 0
    len_my_string = len(my_string)
    len_is_suffix = len(is_suffix)
    if len_my_string < len_is_suffix:
        return answer
    for i in range(len_is_suffix):
        if my_string[len_my_string -1 - i] != is_suffix[len_is_suffix -1 -i]:
            return answer
    answer = 1
        
    return answer