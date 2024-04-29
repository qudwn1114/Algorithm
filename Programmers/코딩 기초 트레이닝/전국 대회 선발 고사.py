def solution(rank, attendance):
    top3 = []
    for i in range(len(rank)):
        idx = rank.index(i+1)
        if attendance[idx]:
            top3.append(idx)
        if len(top3) == 3:
            break
    answer = 10000 * top3[0] + 100 * top3[1] + top3[2]
    return answer