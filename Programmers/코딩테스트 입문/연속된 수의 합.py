def solution(num, total):
    answer = []
    # n * x + n-1(n)/2 = total
    x  = (total - (num-1)*num / 2) // num
    for i in range(num):
        answer.append(x)
        x += 1
    
    return answer

