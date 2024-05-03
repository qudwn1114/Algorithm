def solution(nums):
    answer = len(nums) // 2
    p = {}
    for i in nums:
        if p.get(i):
            p[i] += 1
        else:
            p[i] = 1
    if answer > len(p):
        answer = len(p)
    return answer