def solution(operations):
    arr = []
    for i in operations:
        s, n = i.split(" ")
        if s == "I":
            arr.append(int(n))
        else:
            if arr:
                if n == "1":
                    arr.sort()
                else:
                    arr.sort(reverse=True)
                arr.pop()
    if arr:
        answer = [max(arr), min(arr)]
    else:
        answer = [0, 0]
    return answer