def solution(num_list):
    last_idx = len(num_list) - 1
    if num_list[last_idx] > num_list[last_idx - 1]:
        num_list.append(num_list[last_idx] - num_list[last_idx - 1])
    else:
        num_list.append(num_list[last_idx] * 2)
        
    return num_list