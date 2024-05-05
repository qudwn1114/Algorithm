def solution(priorities, location):
    answer = 0
    q = []
    for i in range(len(priorities)):
        q.append((i, priorities[i]))

    while q:
        max_idx = 0
        max_priority = q[0][1]
        for i in range(len(q)):
            if q[i][1] > max_priority:
                max_priority = q[i][1]
                max_idx = i    
        if q[max_idx][0] == location:
            answer += 1
            break
        else:
            if max_idx == 0 or max_idx == len(q) - 1:
                del q[max_idx]
            else:
                q = q[max_idx+1:] + q[:max_idx]
            answer += 1
    return answer