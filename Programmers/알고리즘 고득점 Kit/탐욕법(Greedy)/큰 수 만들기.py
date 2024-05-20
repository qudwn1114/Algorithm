def solution(number, k):
    s = []

    for i in number:
        while s and s[-1] < i and k > 0:
            s.pop()
            k -= 1
        s.append(i)
    
    s = s[:len(s)-k]
    answer = ''.join(s)
    return answer
