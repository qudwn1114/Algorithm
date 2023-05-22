def solution(stones, k):
    answer = 0
    left = 1
    right = max(stones)

    if k == 1:
        return min(stones)
        
    while(left <= right):
        # 연속 점프 카운트
        count = 0
        # mid번째 니니즈
        mid = (left+right) // 2
        for s in stones:
            if s <= mid:
                count += 1
            # 연속 끊기면 0으로 초기화
            else:
                count = 0
            if count == k:
                break

        if count < k:
            left = mid +1
        else:
            right = mid -1
            answer = mid

    return answer
