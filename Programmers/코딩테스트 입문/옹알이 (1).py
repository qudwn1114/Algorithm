def solution(babbling):
    answer = 0
    arr = ["aya", "ye", "woo", "ma"]
    for i in babbling:
        s = 0
        for j in arr:
            if j in i:
                s += i.count(j) * len(j)
        if s == len(i):
            answer+=1
    return answer