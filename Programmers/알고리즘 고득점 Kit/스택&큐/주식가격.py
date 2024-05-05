def solution(prices):
    answer = []
    for i in range(len(prices)):
        n = 0
        for j in range(i, len(prices)):
            if i == j:
                continue
            n += 1
            if prices[i] > prices[j]:
                break
        answer.append(n)        
        
    return answer