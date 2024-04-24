def solution(arr):
    answer = 0
    last_arr = arr 
    while True:
        temp_arr = []
        for i in last_arr:
            if i >= 50 and i % 2 == 0:
                temp_arr.append(i//2)
            elif i < 50 and i % 2 == 1:
                temp_arr.append(i*2 + 1)
            else:
                temp_arr.append(i)
        if last_arr == temp_arr:
            break
        last_arr = temp_arr
        answer += 1
                
    return answer