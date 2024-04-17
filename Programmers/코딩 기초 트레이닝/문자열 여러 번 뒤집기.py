def solution(my_string, queries):
    for i in queries:
        reversed_str = ''
        for j in range(i[1], i[0]-1, -1):
            reversed_str += my_string[j]        
        my_string = my_string[0:i[0]] + reversed_str + my_string[i[1]+1:]
    answer = my_string
    return answer
