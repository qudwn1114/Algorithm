def solution(my_string):
    answer = ''
    arr = ['a', 'e', 'i', 'o', 'u']
    for i in my_string:
        if i not in arr:
            answer+=i
        
    return answer