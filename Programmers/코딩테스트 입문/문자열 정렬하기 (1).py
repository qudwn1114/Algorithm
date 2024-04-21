def solution(my_string):
    answer = []
    arr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in my_string:
        if i in arr:
            answer.append(int(i))
    answer.sort()
    
    return answer