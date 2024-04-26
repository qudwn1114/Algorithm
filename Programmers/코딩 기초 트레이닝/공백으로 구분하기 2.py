def solution(my_string):
    answer=[]
    arr = my_string.split(" ")
    for i in arr:
        if i != "":
            answer.append(i)
            
    return answer