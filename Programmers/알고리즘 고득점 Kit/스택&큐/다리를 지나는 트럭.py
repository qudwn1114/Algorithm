def solution(bridge_length, weight, truck_weights):
    answer = 1
    q = [[truck_weights.pop(0), 1]]
    while q:
        total_weight = 0
        for i in range(len(q)):
            total_weight += q[i][0]
            q[i][1] +=1    
        if q[0][1] > bridge_length:
            total_weight -= q[0][0]
            q.pop(0)
        if truck_weights:
            if truck_weights[0] + total_weight <= weight:
                q.append([truck_weights.pop(0), 1])
        answer += 1
    return answer