import heapq

def solution(jobs):
    jobs.sort(key=lambda x:x[0])
    answer = 0
    start = -1
    now = 0
    idx = 0
    q = []
    while idx < len(jobs):
        for i in jobs:
            if start < i[0] <= now:
                heapq.heappush(q, [i[1], i[0]])
        if q:
            x = heapq.heappop(q)
            start = now
            now += x[0]
            answer += (now - x[1])
            idx += 1
        else:
            now += 1
    answer = answer // len(jobs)    
    return answer

# 어려움..