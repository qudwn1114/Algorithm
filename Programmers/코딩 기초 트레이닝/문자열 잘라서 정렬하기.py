def solution(myString):
    answer = []
    arr = myString.split("x")
    arr.sort()
    for i in arr:
        if i != "":
            answer.append(i)
    return answer