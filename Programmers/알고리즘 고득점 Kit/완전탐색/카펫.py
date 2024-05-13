def solution(brown, yellow):
    arr = [1]
    for i in range(2, yellow//2+1):
        if yellow % i == 0:
            arr.append(i)
    w = 0
    h = 0
    for i in arr:
        h = i
        w = yellow // h
        if brown == (w * 2) + (h * 2) + 4:
            break
            
    answer = [w+2, h+2]
    return answer
