def solution(progresses, speeds):
    answer = []
    while progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        if progresses[0] >= 100:
            remove_idx_list = []
            for i in range(len(progresses)):
                if progresses[i] >= 100:
                    remove_idx_list.append(i)
                else:
                    break
            answer.append(len(remove_idx_list))
            del progresses[:len(remove_idx_list)]
            del speeds[:len(remove_idx_list)]
        
    return answer

print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]))