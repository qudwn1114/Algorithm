def solution(genres, plays):
    answer = []
    a = {}
    b = {}
    for i in range(len(genres)):
        if a.get(genres[i]):
            a[genres[i]] += plays[i]
            b[genres[i]].append((i, plays[i]))
        else:
            a[genres[i]] = plays[i]
            b[genres[i]] = [(i, plays[i])]
    sorted_a = sorted(a.items(), key=lambda x:-x[1])
    
    for i in sorted_a:
        c = sorted(b[i[0]], key=lambda x:(-x[1],x[0]))
        answer.append(c[0][0])
        if len(c) >= 2:
            answer.append(c[1][0])
    return answer